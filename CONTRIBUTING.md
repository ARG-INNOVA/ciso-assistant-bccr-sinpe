# Contributing

ARG INNOVA welcomes documented proposals through repository issues and pull requests. English is preferred for repository documentation; Spanish is welcome for regulatory analysis. Keep the two main READMEs aligned.

## Before drafting requirements

1. Identify the official source, title, issuing authority, version, publication and effective dates, exact URL and applicability.
2. Record an article, section or page reference for each proposed requirement.
3. Separate original analysis from quotations or adapted third-party wording. Review redistribution rights before including that wording.
4. Establish whether requirements are mandatory, conditional or informative from the source itself. Do not infer a fixed control count.

## Pull request contents

Explain the change, its source and scope, and the checks performed. Label regulatory interpretations, mappings and untested imports as drafts. Do not include production credentials, customer data, confidential assessments, or third-party documents without reviewed rights.

For original contributions, confirm in the pull request that you hold the necessary rights and authorize the scoped MIT grant in LICENSE. Identify excluded third-party content separately in THIRD_PARTY_NOTICES.md, with its provenance and applicable terms. There is no automatic MIT grant for regulatory text.

Run `python3 scripts/validate_scaffold.py` before submission. For future framework changes, provide the source traceability, selected upstream schema/version, validation results and isolated import evidence required by docs/VALIDATION.md. The current validator is structural only.

## Review and releases

A maintainer reviews structure and provenance; a reviewer competent in the applicable requirements reviews regulatory interpretation. Record reviewers and outcomes. Do not label artifacts verified, assign a release version, or request upstream inclusion until release checks are complete. Changes to the scaffold checker must retain an explicit description of what it validates.
