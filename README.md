# BCCR–SINPE for CISO Assistant

Prepared and maintained by **[ARG INNOVA](https://www.arginnova.com)**. [Español](README.es.md).

Comprehensive assessment library based on Banco Central de Costa Rica NT-RCS, edition 7, effective February 11, 2026.

| Contents | Count |
| --- | ---: |
| Official technical controls | 47 |
| Procedural checklist criteria | 66 |
| Non-assessable context notes | 9 |

The 66 criteria are editorial subdivisions of procedural requirements, not additional official controls. Checklist stages cover preparation (17), report preparation/submission (36), follow-up (6), and incidents/reconnection (7).

## Download and import

- [YAML — comprehensive assessment library](framework/releases/bccr-sinpe-nt-rcs-ed7-evaluacion-integral.yaml)
- [Import instructions](docs/IMPORT.md)
- [Releases and downloads](https://github.com/ARG-INNOVA/ciso-assistant-bccr-sinpe/releases)

Import the YAML through CISO Assistant’s library upload function and create a new assessment. Select technical groups from one category only and retain the four checklist groups. This library uses separate URNs and does not automatically migrate earlier assessments.

Category 1 displays 47 controls (43 mandatory, 4 optional). Category 2 displays 39 (29 mandatory, 10 optional), excluding 8 non-applicable controls. Defaults select all of category 1 and the four checklist groups. Both category classifications appear at the start of every control.

Checklist responses use Compliant / Noncompliant and, for conditional requirements, Not applicable. Answers drive status without numeric scores. Score fields are proposed hidden in new assessments. Overall progress may include checklist items and is not the BCCR regulatory verdict.

## Languages, references and validation

Technical controls preserve official Spanish text and IDs. English translations are unofficial; the Spanish PDF prevails. Suffixes such as 5.4.3.A and 7.A are ARG INNOVA subdivisions, not BCCR numbering.

The user reported successful import and visual review. Checks cover structure, text and applicability, plus 230 cases using official answer logic with in-memory fixtures. No isolated database import test was executed; the user’s installed version was not recorded.

- [Source register](docs/SOURCES.md)
- [Validation scope](docs/VALIDATION.md)
- [Test results](docs/VALIDATION_RESULTS.json)
- [Subdivision traceability](docs/TRACEABILITY.json)
- [Project status](docs/PROJECT_STATUS.md)

## ARG INNOVA

For company information and optional professional services, visit [www.arginnova.com](https://www.arginnova.com).

Credits cover library preparation and unofficial translation; BCCR is the regulatory author. No BCCR or Intuitem endorsement is claimed. Authorized open-source content does not require purchasing services.

## Licensing and contributions

MIT covers authorized original content only. BCCR wording, translations and regulatory adaptations are excluded from the grant. Regulatory reuse follows the project owner’s stated decision and authorization.

[LICENSE](LICENSE) · [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) · [CONTRIBUTING.md](CONTRIBUTING.md).

Publication in this repository is independent of any future acceptance into the official CISO Assistant project.
