"""Validate this instruction-only plugin and build its reproducible release ZIP.

Development dependencies: PyYAML, jsonschema. Not run by plugin recipients.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import tempfile
import zipfile
import shutil
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "career-optimizer"


def validate(root):
    errors = []
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8-sig"))
    schema = json.loads((ROOT / "tests" / "plugin.schema.json").read_text(encoding="utf-8-sig"))
    errors.extend(str(e.message) for e in Draft202012Validator(schema).iter_errors(manifest))
    if manifest.get("name") != "career-optimizer":
        errors.append("Unexpected plugin identity")
    interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
    for key in ("displayName", "shortDescription", "developerName", "category"):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            errors.append(f"Missing interface field: {key}")
    skill = root / "skills" / "career-optimizer" / "SKILL.md"
    content = skill.read_text(encoding="utf-8")
    front = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", content, re.S)
    if not front:
        errors.append("Missing skill frontmatter")
    else:
        meta = yaml.safe_load(front.group(1))
        if meta.get("name") != skill.parent.name or not meta.get("description"):
            errors.append("Invalid skill metadata")
        if meta.get("metadata", {}).get("version") != manifest.get("version"):
            errors.append("Version mismatch")
    ui = yaml.safe_load((skill.parent / "agents" / "openai.yaml").read_text(encoding="utf-8"))
    if "$career-optimizer" not in ui["interface"]["default_prompt"]:
        errors.append("Default prompt does not invoke skill")
    if not 25 <= len(ui["interface"]["short_description"]) <= 64:
        errors.append("Skill short description length invalid")
    for path in root.rglob("*"):
        if path.is_symlink():
            errors.append(f"Symlink not allowed: {path.name}")
        if not path.is_file():
            continue
        if path.suffix not in (".md", ".txt", ".json", ".yaml"):
            errors.append(f"Unexpected runtime file: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        # Generic schema/template field placeholders are intentional; user data is not.
        if re.search(r"[A-Z]:[\\/]Users[\\/]|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{25,}|-----BEGIN .*PRIVATE KEY", text):
            errors.append(f"Possible private data: {path.name}")
        if path.suffix == ".md":
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                if re.match(r"(?:https?://|#|mailto:)", link):
                    continue
                target = (path.parent / link.split("#")[0]).resolve()
                if not target.is_relative_to(root.resolve()) or not target.exists():
                    errors.append(f"Broken or escaping reference: {path.name}: {link}")
    if errors:
        raise ValueError("\n".join(errors))
    return manifest


def negative_tests():
    mutations = [
        lambda p: (p / "plugin.json").write_text('{"name":"INVALID"}', encoding="utf-8"),
        lambda p: (p / "skills/career-optimizer/references/onboarding.md").unlink(),
        lambda p: (p / "skills/career-optimizer/private.txt").write_text("C:/Users/Test/secret", encoding="utf-8"),
    ]
    for i, mutate in enumerate(mutations):
        with tempfile.TemporaryDirectory() as temp:
            candidate = Path(temp) / "plugin"
            shutil.copytree(PLUGIN, candidate)
            mutate(candidate)
            try:
                validate(candidate)
            except (ValueError, KeyError, FileNotFoundError):
                continue
            raise AssertionError(f"Invalid fixture {i} was accepted")
    print("Negative checks passed: malformed manifest, missing reference, private local path")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--negative-tests", action="store_true")
    args = parser.parse_args()
    manifest = validate(PLUGIN)
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    entry = marketplace["plugins"][0]
    assert (ROOT / entry["source"]["path"]).resolve() == PLUGIN.resolve()
    assert entry["name"] == manifest["name"]
    print("PASS: manifest schema, skill YAML, local links, runtime allowlist, marketplace path")
    if args.negative_tests:
        negative_tests()
    if not args.output:
        return
    args.output.mkdir(parents=True, exist_ok=True)
    dest = args.output / f"Career-Optimizer-{manifest['version']}.zip"
    files = sorted(p for p in PLUGIN.rglob("*") if p.is_file())
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            info = zipfile.ZipInfo(path.relative_to(PLUGIN).as_posix(), (2026, 10, 14, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(dest) as archive:
        assert archive.testzip() is None
        assert "plugin.json" in archive.namelist()
        assert len(archive.namelist()) == len(files)
        for path in files:
            assert archive.read(path.relative_to(PLUGIN).as_posix()) == path.read_bytes()
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    (args.output / "SHA256SUMS.txt").write_text(f"{digest}  {dest.name}\n", encoding="utf-8")
    print(json.dumps({"file": str(dest), "files": len(files), "sha256": digest}))


if __name__ == "__main__":
    main()
