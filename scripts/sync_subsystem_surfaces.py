#!/usr/bin/env python3
import json
from pathlib import Path
from collections import OrderedDict


ROOT = Path(__file__).resolve().parent.parent
SYSTEMS_DIR = ROOT / "systems"
CONTEXT_PATH = ROOT / "meta" / "subsystem_human_context.yaml"
EXPORT_DIR = ROOT / "meta" / "exports"


def load_json_yaml(path: Path):
    return json.loads(path.read_text())


def rel(from_path: Path, to_path: Path) -> str:
    return Path(
        Path(
            __import__("os").path.relpath(to_path, start=from_path.parent)
        )
    ).as_posix()


def main():
    context = load_json_yaml(CONTEXT_PATH)
    manifests = {}
    for manifest_path in sorted(SYSTEMS_DIR.rglob("manifest.yaml")):
        manifest = load_json_yaml(manifest_path)
        manifests[manifest["id"]] = (manifest, manifest_path)

    rows = []
    for subsystem_id, (manifest, manifest_path) in sorted(manifests.items()):
        subsystem_dir = manifest_path.parent
        overview_path = subsystem_dir / "OVERVIEW.md"
        ctx = context[subsystem_id]
        parent = manifest.get("parent")
        children = manifest.get("owned_subsystems", [])
        if not children:
            registry_rel = manifest.get("registry")
            if registry_rel:
                registry = load_json_yaml(ROOT / registry_rel)
                children = registry.get("subsystems", [])

        readme_path = subsystem_dir / "README.md"
        schema_path = ROOT / manifest["canonical_schema"]
        schema_surface = subsystem_dir / "SCHEMA.md" if (subsystem_dir / "SCHEMA.md").exists() else None
        contracts_path = subsystem_dir / "contracts" / "README.md"
        tests_path = subsystem_dir / "tests" / "README.md"

        lines = []
        lines.append("---")
        lines.append(f"title: {subsystem_id} Overview")
        lines.append(f"status: {manifest.get('status', 'bounded')}")
        tags = list(OrderedDict.fromkeys([
            "subsystem",
            "overview",
            subsystem_id.split('/')[0],
            manifest.get("kind", "unknown"),
            manifest.get("status", "unknown"),
            subsystem_id.replace("/", "-"),
            *subsystem_id.split("/"),
        ]))
        lines.append("tags:")
        for tag in tags:
            lines.append(f"  - {tag}")
        lines.append("---")
        lines.append("")
        lines.append(f"# {subsystem_id} Overview")
        lines.append("")
        lines.append("## Who")
        for actor in ctx["actors"]:
            lines.append(f"- {actor}")
        lines.append("")
        lines.append("## What")
        lines.append("")
        lines.append(ctx["summary"])
        lines.append("")
        lines.append("## Why")
        lines.append("")
        lines.append(ctx["rationale"])
        lines.append("")
        lines.append("## Where")
        lines.append("")
        lines.append(f"- Path: `{subsystem_dir.relative_to(ROOT).as_posix()}`")
        lines.append(f"- Kind: `{manifest.get('kind', 'unknown')}`")
        lines.append(f"- Status: `{manifest.get('status', 'unknown')}`")
        lines.append(f"- Parent: `{parent or 'none'}`")
        lines.append(f"- Depends on: `{', '.join(manifest.get('depends_on', [])) or 'none'}`")
        lines.append(f"- Allowed dependencies: `{', '.join(manifest.get('allowed_dependencies', [])) or 'none'}`")
        lines.append(f"- Child subsystems: `{', '.join(children) or 'none'}`")
        lines.append("")
        lines.append("## How")
        lines.append("")
        lines.append(f"- Canonical schema: [{schema_path.name}]({rel(overview_path, schema_path)})")
        lines.append(f"- Local readme: [{readme_path.name}]({rel(overview_path, readme_path)})")
        if schema_surface:
            lines.append(f"- Local schema surface: [{schema_surface.name}]({rel(overview_path, schema_surface)})")
        if contracts_path.exists():
            lines.append(f"- Contracts surface: [{contracts_path.parent.name}]({rel(overview_path, contracts_path)})")
        if tests_path.exists():
            lines.append(f"- Tests surface: [{tests_path.parent.name}]({rel(overview_path, tests_path)})")
        lines.append(f"- Validator: `python3 scripts/validate_subsystems.py`")
        lines.append("")
        lines.append("## When")
        lines.append("")
        lines.append(ctx["touch_when"])
        lines.append("")
        lines.append("## Truth Surfaces")
        lines.append("")
        lines.append(f"- Manifest: [{manifest_path.name}]({rel(overview_path, manifest_path)})")
        lines.append(f"- Canonical schema: [{schema_path.name}]({rel(overview_path, schema_path)})")
        if schema_surface:
            lines.append(f"- Local schema surface: [{schema_surface.name}]({rel(overview_path, schema_surface)})")
        overview_path.write_text("\n".join(lines) + "\n")

        rows.append({
            "id": subsystem_id,
            "status": manifest.get("status", "unknown"),
            "parent": parent,
            "kind": manifest.get("kind", "unknown"),
            "path": subsystem_dir.relative_to(ROOT).as_posix(),
            "summary": ctx["summary"],
            "actors": ctx["actors"],
            "rationale": ctx["rationale"],
            "touch_when": ctx["touch_when"],
            "depends_on": manifest.get("depends_on", []),
            "allowed_dependencies": manifest.get("allowed_dependencies", []),
            "child_subsystems": children,
            "manifest": manifest_path.relative_to(ROOT).as_posix(),
            "canonical_schema": manifest["canonical_schema"],
            "readme": readme_path.relative_to(ROOT).as_posix(),
            "schema_surface": schema_surface.relative_to(ROOT).as_posix() if schema_surface else None,
            "overview": overview_path.relative_to(ROOT).as_posix(),
        })

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    (EXPORT_DIR / "subsystem_human_index.json").write_text(
        json.dumps({"subsystems": rows}, indent=2, sort_keys=True) + "\n"
    )

    md = []
    md.append("---")
    md.append("title: Subsystem Human Index")
    md.append("status: canonical")
    md.append("tags:")
    md.append("  - subsystem-index")
    md.append("  - human-readable")
    md.append("  - who-what-when-where-how-why")
    md.append("  - architecture")
    md.append("---")
    md.append("")
    md.append("# Subsystem Human Index")
    md.append("")
    md.append("| ID | Status | Parent | Overview | Summary |")
    md.append("| --- | --- | --- | --- | --- |")
    for row in rows:
        overview_rel = row["overview"]
        md.append(
            f"| `{row['id']}` | `{row['status']}` | `{row['parent'] or 'none'}` | [{Path(overview_rel).name}](/home/admin1/blackflag-cathedral/{overview_rel}) | {row['summary']} |"
        )
    (EXPORT_DIR / "subsystem_human_index.md").write_text("\n".join(md) + "\n")


if __name__ == "__main__":
    main()
