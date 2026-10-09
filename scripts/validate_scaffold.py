"""Validate repository preparation only; never assert framework compliance."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['.github/workflows/validate-scaffold.yml', '.gitignore', 'CHANGELOG.md', 'CONTRIBUTING.md', 'LICENSE', 'README.es.md', 'README.md', 'THIRD_PARTY_NOTICES.md', 'docs/IMPORT.md', 'docs/LICENSING.md', 'docs/PROJECT_STATUS.md', 'docs/SOURCES.md', 'docs/UPLOAD.es.md', 'docs/VALIDATION.md', 'framework/README.md', 'framework/drafts/README.md', 'framework/drafts/REQUIREMENT_TEMPLATE.md', 'framework/metadata.json', 'framework/releases/README.md', 'mappings/MAPPING_TEMPLATE.md', 'mappings/README.md', 'scripts/validate_scaffold.py']

def validate():
    errors = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file() or path.stat().st_size == 0:
            errors.append("Missing or empty required file: " + name)
    try:
        data = json.loads((ROOT / "framework/metadata.json").read_text(encoding="utf-8"))
        expected = {'project': 'ciso-assistant-bccr-sinpe', 'maintainer': 'ARG INNOVA', 'status': 'scaffold', 'regulatory_sources': [], 'verified_control_count': None, 'ciso_assistant_version': None, 'framework_release': None, 'import_tested': False}
        if data != expected:
            errors.append("Scaffold metadata changed: review status and extend validation before claiming a framework release.")
    except (OSError, ValueError) as exc:
        errors.append("Invalid metadata: " + str(exc))
    text_paths = set(ROOT.rglob("*.md")) | set(ROOT.rglob("*.py")) | set(ROOT.rglob("*.json"))
    text_paths |= {ROOT / "LICENSE", ROOT / ".gitignore", ROOT / ".github/workflows/validate-scaffold.yml"}
    for path in sorted(text_paths):
        if any(part in {".git", ".venv", "venv", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        if not path.is_file():
            continue
        try:
            body = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(str(path.relative_to(ROOT)) + ": " + str(exc))
            continue
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", body):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                local = (path.parent / unquote(parsed.path)).resolve()
                if ROOT not in local.parents and local != ROOT:
                    errors.append("Local link escapes repository: " + target)
                elif not local.exists():
                    errors.append(str(path.relative_to(ROOT)) + ": missing local link " + target)
    artifacts = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "framework").rglob("*")
                       if p.is_file() and p.suffix.lower() in {".xlsx", ".xls", ".yaml", ".yml"})
    if artifacts:
        print("WARNING: Framework artifacts are NOT validated: " + ", ".join(artifacts))
    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1
    print("PASS: required scaffold files, status metadata, UTF-8 and local Markdown link targets.")
    print("PENDING: regulatory review, control inventory, Excel/YAML validation and CISO Assistant import tests.")
    return 0

if __name__ == "__main__":
    sys.exit(validate())
