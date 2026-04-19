#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SYSTEMS_DIR = ROOT / "systems"
EXPORT_DIR = ROOT / "meta" / "exports"


def load_json_yaml(path: Path):
    return json.loads(path.read_text())


def main():
    manifests = {}
    for manifest_path in sorted(SYSTEMS_DIR.rglob("manifest.yaml")):
        manifest = load_json_yaml(manifest_path)
        manifests[manifest["id"]] = manifest

    graph = {
        "subsystems": {},
        "edges": [],
    }

    for subsystem_id, manifest in sorted(manifests.items()):
        graph["subsystems"][subsystem_id] = {
            "kind": manifest.get("kind"),
            "status": manifest.get("status"),
            "parent": manifest.get("parent"),
            "depends_on": manifest.get("depends_on", []),
            "allowed_dependencies": manifest.get("allowed_dependencies", []),
        }

        parent = manifest.get("parent")
        if parent:
            graph["edges"].append(
                {"from": parent, "to": subsystem_id, "kind": "contains"}
            )

        for dep in manifest.get("depends_on", []):
            graph["edges"].append(
                {"from": subsystem_id, "to": dep, "kind": "depends_on"}
            )

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    (EXPORT_DIR / "subsystem_graph.json").write_text(
        json.dumps(graph, indent=2, sort_keys=True) + "\n"
    )

    mermaid = ["graph TD"]
    for edge in graph["edges"]:
        left = normalize(edge["from"])
        right = normalize(edge["to"])
        label = "contains" if edge["kind"] == "contains" else "depends_on"
        mermaid.append(f"  {left} -->|{label}| {right}")

    (EXPORT_DIR / "subsystem_graph.mmd").write_text("\n".join(mermaid) + "\n")


def normalize(value: str) -> str:
    return (
        value.replace("-", "_")
        .replace("/", "__")
        .replace(".", "_")
    )


if __name__ == "__main__":
    main()

