# BCCR–SINPE for CISO Assistant

Prepared by [ARG INNOVA](https://www.arginnova.com). [Español](README.es.md).

**Package v0.1.2.** Two category-specific compliance libraries based on BCCR NT-RCS edition 7, effective February 11, 2026. [PR #5032](https://github.com/intuitem/ciso-assistant-community/pull/5032) remains pending upstream acceptance. This package is independent of an official CISO Assistant distribution.

| Library | Technical controls | Mandatory | Optional | Checklist | Assessable total | Internal YAML version |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Category 1 | 47 | 43 | 4 | 66 | 113 | 3 |
| Category 2 | 39 | 29 | 10 | 66 | 105 | 1 |

Each library also contains 9 non-assessable context notes. The 66 procedural checklist criteria are editorial subdivisions, not additional official controls. English translations are unofficial; the Spanish BCCR source prevails.

## Download and import

- [Category 1 YAML](framework/releases/bccr-sinpe-nt-rcs-ed7-evaluacion-integral.yaml)
- [Category 2 YAML](framework/releases/bccr-sinpe-nt-rcs-ed7-evaluacion-integral-cat2.yaml)
- [Releases and ZIP](https://github.com/ARG-INNOVA/ciso-assistant-bccr-sinpe/releases)
- [Import and upgrade guide](docs/IMPORT.md)

Import the YAML for the entity's connection category and create a new assessment. There are no category or checklist implementation groups to select. Do not combine category libraries in one audit. Package version 0.1.2 is distinct from internal YAML versions 3 and 1. Automatic migration of earlier assessment answers is not provided or verified.

## Compliance and mitigation

All technical controls have Compliant / Noncompliant questions. All procedural criteria also offer Not applicable, requiring a documented absent triggering condition or event. It must not replace pending review, missing evidence or an applicable obligation. Unanswered requirements remain unassessed.

Choices use `compute_result` without `add_score`. No maturity scale is introduced. A default 0–100 range may appear on the framework detail page; the tested questionnaires had no editable score fields. Status percentages and progress do not establish a regulatory verdict or compensate for a failed mandatory control.

Track mitigation using applied controls, owners, target dates, status, progress and evidence. The libraries do not create actions automatically. Auditors must review evidence before revising compliance results. A complete mitigation lifecycle has not yet been tested.

## Validation and references

Both libraries were imported into a live instance and four result states were tested with synthetic answers. An additional 786 cases used native functions with in-memory fixtures. Full application suites and direct database score checks were not performed. The installed application version was not recorded.

- [Validation scope](docs/VALIDATION.md)
- [Validation results](docs/VALIDATION_RESULTS.json)
- [Anonymized live checks](docs/LIVE_VALIDATION.json)
- [Traceability](docs/TRACEABILITY.json)
- [Sources](docs/SOURCES.md)
- [Changelog](CHANGELOG.md)

## Licensing and contributions

Regulatory author: Banco Central de Costa Rica. Packaging and unofficial translation: ARG INNOVA. No BCCR or Intuitem endorsement is claimed. MIT covers authorized original content only; BCCR wording, translations and regulatory adaptations remain excluded. Existing regulatory reuse terms are unchanged.

[LICENSE](LICENSE) · [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) · [CONTRIBUTING.md](CONTRIBUTING.md).
