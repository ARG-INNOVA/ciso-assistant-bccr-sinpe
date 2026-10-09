# BCCR–SINPE for CISO Assistant

Initial repository scaffold maintained by **ARG INNOVA** for a planned Costa Rica BCCR–SINPE cybersecurity compliance library for CISO Assistant.

**Status: preparation only.** No final Excel workbook, importable framework YAML, verified control inventory, or completed cross-framework mapping is included. No claim of 47 verified controls is made. The applicable regulatory documents, versions, effective dates and scope still require review. CISO Assistant compatibility has not been tested.

[Español](README.es.md)

## Purpose and scope

Prepare a traceable, reviewed representation of applicable BCCR–SINPE requirements for use in CISO Assistant. Determine applicability, source versions and requirement boundaries before drafting controls. This is an independent community initiative; BCCR and Intuitem endorsement or affiliation is not claimed. This scaffold does not establish compliance or constitute legal advice.

## Repository layout

```text
.github/workflows/validate-scaffold.yml  Structural checks only
framework/                             Future artifacts and status metadata
framework/drafts/                      Drafting instructions; no control content
framework/releases/                    Reserved for reviewed import artifacts
mappings/                              Mapping methodology and blank template
scripts/validate_scaffold.py            Dependency-free structural validator
docs/                                  Sources, licensing, validation and publishing
CONTRIBUTING.md                         Contribution and review process
CHANGELOG.md                            Unreleased scaffold changes
LICENSE                                MIT grant for original content only
THIRD_PARTY_NOTICES.md                  Regulatory and third-party exclusions
```

## Getting started

1. Read [project status](docs/PROJECT_STATUS.md) and [source register](docs/SOURCES.md).
2. Follow [upload instructions](docs/UPLOAD.es.md) to place this scaffold at the repository root.
3. Run `python3 scripts/validate_scaffold.py` from the repository root (Python 3.9+).
4. Complete the source register, regulatory review and [release checklist](docs/VALIDATION.md) before producing a framework release.

The GitHub Actions workflow runs structural checks on pushes and pull requests and can be triggered manually. A passing run means only that the scaffold checks passed. It does not validate regulatory content, Excel/YAML schemas, mappings or import behavior.

## Importing into CISO Assistant

There is currently **nothing to import**. See [future import validation](docs/IMPORT.md). Select and record an upstream CISO Assistant version or commit and its documented library format before preparing any workbook or YAML. Do not rename placeholders to importable file extensions.

## Licensing and contributions

The [MIT license](LICENSE) applies only to original content whose rights holders authorize that grant. BCCR regulations, publications, quotations, logos and other third-party content are excluded; see [licensing policy](docs/LICENSING.md) and [third-party notices](THIRD_PARTY_NOTICES.md). This repository grants no rights to that excluded material.

Use [CONTRIBUTING.md](CONTRIBUTING.md) for changes. Proposals are reviewed through GitHub issues and pull requests; no external email address is assumed.

## Official references

- [Banco Central de Costa Rica](https://www.bccr.fi.cr/) — discovery starting point, not a selected regulatory baseline.
- [CISO Assistant upstream repository](https://github.com/intuitem/ciso-assistant-community) — format and contribution guidance to verify against the selected version.

Reference links do not imply regulatory validation or upstream acceptance.
