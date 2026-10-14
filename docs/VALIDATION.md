# Validation of package v0.1.2

The two category libraries passed structural/content regressions and 786 result-recomputation cases using native functions from upstream base commit 75b4788 with in-memory fixtures. Source text hashes cover 47 technical controls in category 1 and its 39 applicable controls in category 2. These checks are not a database integration test.

Both libraries were subsequently imported into an actual CISO Assistant instance on 2026-10-14. Interface checks confirmed 113/105 assessable requirements, the displayed category classification and 47/39 technical questions plus 66 procedural questions each. Synthetic answers produced compliant, noncompliant and procedural not-applicable results; unanswered requirements stayed unassessed. Results persisted after returning to each audit summary. No editable score fields appeared in the questionnaires.

The live 43/4 and 29/10 counts were verified from imported classification text. Native importance fields and numeric scores were not queried directly in the database. The default framework 0–100 metadata range remained visible. Installed application version was not recorded. Tests do not certify an organization's compliance or imply upstream acceptance.

The complete mitigation lifecycle, assignments, notifications, evidence upload and action closure remain untested. Full backend/frontend suites were not run for this package.

[Machine-readable results](VALIDATION_RESULTS.json) · [Anonymized live checks](LIVE_VALIDATION.json)

Run `python scripts/validate_scaffold.py` after installing `scripts/requirements-validation.txt`. This validates repository links, metadata, category libraries, source hashes and traceability. The GitHub workflow executes the same command.
