# Validation and release checklist

## Current automated checks

Run `python3 scripts/validate_scaffold.py` from the repository root using Python 3.9 or newer. The script checks required nonempty files, valid scaffold metadata, UTF-8 text and existing local Markdown link targets. It reports any future Excel/YAML framework files as outside its validation scope. It uses only the Python standard library.

The workflow at `.github/workflows/validate-scaffold.yml` executes that same script. It follows [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), has read-only repository permissions and no deployment step. Workflow execution on GitHub must be observed after upload; local script success does not prove a GitHub run occurred.

**A successful structural check is not framework validation.** The current workflow is provisional with respect to regulatory content and CISO Assistant compatibility. When adding real artifacts, extend or replace these checks and update the workflow name and documentation to match the actual checks.

## Required before the first framework release

- [ ] Official source register completed, with version, effective dates and applicability.
- [ ] Redistribution rights reviewed; excluded material documented separately.
- [ ] Every requirement traced to an exact source location and reviewed.
- [ ] Stable unique identifiers, hierarchy and mandatory/conditional treatment checked.
- [ ] Control count derived from the reviewed inventory, with no assumed target count.
- [ ] CISO Assistant version or commit and documented format selected and recorded.
- [ ] Workbook/YAML syntax, schema and semantic validation implemented for that version.
- [ ] Duplicates, missing fields, broken references and conversion consistency checked.
- [ ] Import into an isolated CISO Assistant instance completed and evidence recorded.
- [ ] Displayed hierarchy, counts, language, references and licensing notices checked after import.
- [ ] Mappings independently reviewed if included; none inferred as equivalent by default.
- [ ] Reviewer names, dates, artifact checksums, known limitations and release notes recorded.

Keep validation evidence with the release documentation. Do not treat this checklist, a placeholder or a green scaffold workflow as proof that any item has been completed.
