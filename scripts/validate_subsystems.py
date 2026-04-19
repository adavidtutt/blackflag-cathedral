#!/usr/bin/env python3
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SYSTEMS_DIR = ROOT / "systems"
CONTEXT_PATH = ROOT / "meta" / "subsystem_human_context.yaml"


def load_json_yaml(path: Path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise RuntimeError(f"failed to parse {path}: {exc}") from exc


def find_manifests():
    return sorted(SYSTEMS_DIR.rglob("manifest.yaml"))


def main():
    errors = []

    registry_path = SYSTEMS_DIR / "REGISTRY.yaml"
    if not registry_path.exists():
      errors.append("missing systems/REGISTRY.yaml")
      print_errors(errors)
      return 1

    root_registry = load_json_yaml(registry_path)
    top_level = root_registry.get("top_level_subsystems", [])
    context = load_json_yaml(CONTEXT_PATH)

    manifests = {}
    manifest_paths = {}

    for manifest_path in find_manifests():
        manifest = load_json_yaml(manifest_path)
        subsystem_id = manifest.get("id")
        if not subsystem_id:
            errors.append(f"{manifest_path}: missing id")
            continue
        if subsystem_id in manifests:
            errors.append(f"duplicate subsystem id: {subsystem_id}")
            continue
        manifests[subsystem_id] = manifest
        manifest_paths[subsystem_id] = manifest_path

    for subsystem_id in top_level:
        if subsystem_id not in manifests:
            errors.append(f"top-level subsystem missing manifest: {subsystem_id}")

    for subsystem_id, manifest in manifests.items():
        manifest_path = manifest_paths[subsystem_id]
        subsystem_dir = manifest_path.parent
        parent = manifest.get("parent")
        if parent and parent not in manifests:
            errors.append(f"{subsystem_id}: missing parent manifest {parent}")

        if subsystem_id not in context:
            errors.append(f"{subsystem_id}: missing human context entry")

        if not manifest.get("canonical_schema"):
            errors.append(f"{subsystem_id}: missing canonical_schema")
        else:
            schema_path = ROOT / manifest["canonical_schema"]
            if not schema_path.exists():
                errors.append(f"{subsystem_id}: canonical_schema path missing {manifest['canonical_schema']}")

        for rel_key in ["readme", "schema_surface"]:
            rel_path = manifest.get(rel_key)
            if rel_path and not (ROOT / rel_path).exists():
                errors.append(f"{subsystem_id}: referenced path missing {rel_path}")

        depends_on = manifest.get("depends_on", [])
        allowed_deps = manifest.get("allowed_dependencies", [])
        for dep in depends_on:
            if dep not in manifests:
                errors.append(f"{subsystem_id}: missing dependency {dep}")
            if allowed_deps and dep not in allowed_deps:
                errors.append(f"{subsystem_id}: dependency {dep} not present in allowed_dependencies")

        readme_path = subsystem_dir / "README.md"
        if not readme_path.exists():
            errors.append(f"{subsystem_id}: missing README.md")

        overview_path = subsystem_dir / "OVERVIEW.md"
        if not overview_path.exists():
            errors.append(f"{subsystem_id}: missing OVERVIEW.md")

        is_top_level = manifest.get("kind") == "top-level-subsystem"
        is_composite = bool(manifest.get("registry")) or bool(manifest.get("owned_subsystems"))
        is_fcs_contract_layer = (
            subsystem_id.startswith("cathedral/fractal-cognitive-substrate/")
            and subsystem_id != "cathedral/fractal-cognitive-substrate"
        )

        if is_top_level:
            for required_key in ["readme", "schema_surface", "registry", "owned_subsystems"]:
                if required_key not in manifest:
                    errors.append(f"{subsystem_id}: missing required top-level key {required_key}")

        if is_composite:
            for required_key in ["readme", "schema_surface", "registry", "owned_subsystems"]:
                if required_key not in manifest:
                    errors.append(f"{subsystem_id}: missing required composite key {required_key}")

            for rel_path in [manifest.get("readme"), manifest.get("schema_surface"), manifest.get("registry")]:
                if rel_path and not (ROOT / rel_path).exists():
                    errors.append(f"{subsystem_id}: referenced path missing {rel_path}")

            subsystem_registry_readme = subsystem_dir / "subsystems" / "README.md"
            contracts_readme = subsystem_dir / "contracts" / "README.md"
            tests_readme = subsystem_dir / "tests" / "README.md"
            if not subsystem_registry_readme.exists():
                errors.append(f"{subsystem_id}: missing subsystems/README.md")
            if not contracts_readme.exists():
                errors.append(f"{subsystem_id}: missing contracts/README.md")
            if not tests_readme.exists():
                errors.append(f"{subsystem_id}: missing tests/README.md")

        if is_fcs_contract_layer:
            for required_key in ["readme", "schema_surface", "contract_node"]:
                if required_key not in manifest:
                    errors.append(f"{subsystem_id}: missing required FCS contract-layer key {required_key}")

            contracts_readme = subsystem_dir / "contracts" / "README.md"
            tests_readme = subsystem_dir / "tests" / "README.md"
            if not contracts_readme.exists():
                errors.append(f"{subsystem_id}: missing contracts/README.md")
            if not tests_readme.exists():
                errors.append(f"{subsystem_id}: missing tests/README.md")

            contract_node = manifest.get("contract_node", {})
            for required_key in ["node_class", "owns", "requires", "emits_to", "forbids"]:
                if required_key not in contract_node:
                    errors.append(f"{subsystem_id}: contract_node missing {required_key}")

            owns = contract_node.get("owns", [])
            requires = contract_node.get("requires", [])
            emits_to = contract_node.get("emits_to", [])
            forbids = contract_node.get("forbids", [])

            if not isinstance(owns, list) or not owns:
                errors.append(f"{subsystem_id}: contract_node owns must be a non-empty list")
            if not isinstance(requires, list):
                errors.append(f"{subsystem_id}: contract_node requires must be a list")
            if not isinstance(emits_to, list):
                errors.append(f"{subsystem_id}: contract_node emits_to must be a list")
            if not isinstance(forbids, list) or not forbids:
                errors.append(f"{subsystem_id}: contract_node forbids must be a non-empty list")

            if sorted(requires) != sorted(depends_on):
                errors.append(f"{subsystem_id}: contract_node requires must match depends_on exactly")

            for dep in emits_to:
                if dep not in manifests:
                    errors.append(f"{subsystem_id}: contract_node emits_to target missing {dep}")
                if allowed_deps and dep not in allowed_deps:
                    errors.append(f"{subsystem_id}: contract_node emits_to target {dep} not present in allowed_dependencies")

        owned = manifest.get("owned_subsystems", [])
        registry_rel = manifest.get("registry")
        if registry_rel:
            registry_file = ROOT / registry_rel
            if not registry_file.exists():
                errors.append(f"{subsystem_id}: missing registry file {registry_rel}")
            else:
                registry = load_json_yaml(registry_file)
                registry_children = registry.get("subsystems", [])
                if owned and owned != registry_children:
                    errors.append(
                        f"{subsystem_id}: owned_subsystems and registry contents differ"
                    )
                for child in registry_children:
                    if child not in manifests:
                        errors.append(f"{subsystem_id}: child listed in registry missing manifest {child}")
                    elif manifests[child].get("parent") != subsystem_id:
                        errors.append(f"{subsystem_id}: child {child} does not point back to parent")

    for subsystem_id in context:
        if subsystem_id not in manifests:
            errors.append(f"human context entry without manifest: {subsystem_id}")

    for export_rel in [
        "meta/exports/subsystem_graph.json",
        "meta/exports/subsystem_graph.mmd",
        "meta/exports/subsystem_human_index.json",
        "meta/exports/subsystem_human_index.md",
    ]:
        if not (ROOT / export_rel).exists():
            errors.append(f"missing export artifact {export_rel}")

    if errors:
        print_errors(errors)
        return 1

    print("Subsystem graph validation passed.")
    print(f"Top-level subsystems: {len(top_level)}")
    print(f"All manifests: {len(manifests)}")
    for subsystem_id in sorted(manifests):
        print(f"- {subsystem_id}")
    return 0


def print_errors(errors):
    print("Subsystem graph validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
