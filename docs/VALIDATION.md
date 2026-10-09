# Validation scope / Alcance de validación

[VALIDATION_RESULTS.json](VALIDATION_RESULTS.json) records the performed checks. The user subsequently reported successful import and visual review; the application version is unknown. The recorded isolated database import remains unperformed, distinct from the user’s report.

The repository checker verifies required files, local links, metadata counts, YAML node uniqueness and parent/depth integrity, bilingual content, procedural traceability coverage, unchanged technical applicability, stage groups and result-only checklist choice configuration. It does not certify regulatory interpretation, reproduce the application database or run the full CISO Assistant suite.

Native status/score behavior was checked separately in 230 cases with official functions and in-memory fixtures. Details and pinned upstream commit are in the results file. External consultant review is optional.

```sh
python3 -m pip install -r scripts/requirements-validation.txt
python3 scripts/validate_scaffold.py
```

Changing source content, conditions, groups or status logic requires revisiting validation; a green workflow is not a compliance verdict.

Version 2 adds a regression check: 6.3.3 must belong to both complete category groups and display Optional/Optional. The repository check also verifies all 47 original bodies after the classification prefix. User reimport of version 2 has not yet been reported.
