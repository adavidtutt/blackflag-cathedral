#!/usr/bin/env python3
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SYSTEMS_DIR = ROOT / "systems"


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
        parent = manifest.get("parent")
        if parent and parent not in manifests:
            errors.append(f"{subsystem_id}: missing parent manifest {parent}")

        for dep in manifest.get("depends_on", []):
            if dep not in manifests:
                errors.append(f"{subsystem_id}: missing dependency {dep}")

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

