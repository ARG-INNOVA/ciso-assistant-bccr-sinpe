# BCCR–SINPE para CISO Assistant

Preparado por [ARG INNOVA](https://www.arginnova.com). [English](README.md).

**Paquete v0.1.2.** Dos bibliotecas de evaluación por categoría basadas en NT-RCS edición 7, vigente desde el 11/02/2026. La contribución [PR #5032](https://github.com/intuitem/ciso-assistant-community/pull/5032) está pendiente de aceptación en CISO Assistant; este paquete es independiente del producto oficial.

| Biblioteca | Controles técnicos | Obligatorios | Opcionales | Checklist | Total evaluable | Versión interna YAML |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Categoría 1 | 47 | 43 | 4 | 66 | 113 | 3 |
| Categoría 2 | 39 | 29 | 10 | 66 | 105 | 1 |

Cada biblioteca incluye 9 notas no evaluables. Los 66 criterios son desgloses editoriales procedimentales, no controles oficiales adicionales. Inglés: traducción no oficial; prevalece el texto español del BCCR.

## Descargar e importar

- [Categoría 1](framework/releases/bccr-sinpe-nt-rcs-ed7-evaluacion-integral.yaml)
- [Categoría 2](framework/releases/bccr-sinpe-nt-rcs-ed7-evaluacion-integral-cat2.yaml)
- [Releases y ZIP](https://github.com/ARG-INNOVA/ciso-assistant-bccr-sinpe/releases)
- [Guía de importación y actualización](docs/IMPORT.md)

Importe el YAML de la categoría de conexión correspondiente y cree una evaluación nueva. Ya no hay grupos `cat1`/`cat2` ni grupos de checklist que seleccionar. No combine las dos bibliotecas en una auditoría. El número del paquete (0.1.2) es independiente de la versión interna de cada YAML (3 y 1). No se promete migración automática de auditorías anteriores.

## Resultados y mitigaciones

Todos los controles técnicos incluyen Cumple / No cumple. Los criterios procedimentales también ofrecen No aplica, que exige justificar la ausencia de la condición o evento aplicable; no sustituye una revisión pendiente, falta de evidencia ni una obligación aplicable. Sin respuesta, el requisito sigue sin evaluar.

Las respuestas usan `compute_result` sin `add_score`. No se introduce una escala de madurez. El rango 0–100 puede aparecer como metadato de la ficha del framework; las pruebas de cuestionario no mostraron campos editables de puntuación. Los porcentajes de estados y avance no son un dictamen regulatorio: un incumplimiento obligatorio no queda compensado por un promedio.

Gestione las acciones correctivas con controles aplicados, responsable, fecha objetivo, estado, avance y evidencia. La biblioteca no crea acciones automáticamente. La evidencia debe revisarse antes de cambiar el resultado de cumplimiento. El ciclo completo de mitigación todavía no se ha probado.

## Validación y referencias

Ambas bibliotecas se importaron en una instancia real y se probaron los cuatro estados con datos sintéticos. Hay 786 casos adicionales con funciones nativas y objetos en memoria. No se ejecutaron las suites completas de la aplicación ni se verificó el score directamente en base de datos. La versión instalada no fue registrada.

- [Validación y límites](docs/VALIDATION.md)
- [Resultados reproducibles](docs/VALIDATION_RESULTS.json)
- [Resumen anónimo de pruebas de interfaz](docs/LIVE_VALIDATION.json)
- [Trazabilidad](docs/TRACEABILITY.json)
- [Fuentes](docs/SOURCES.md)
- [Historial](CHANGELOG.md)

## Licencia y contribuciones

La autoría normativa corresponde al BCCR. El empaquetado y las traducciones no oficiales son de ARG INNOVA. No se afirma aval del BCCR ni de Intuitem. MIT se limita al contenido original autorizado y excluye texto BCCR, traducciones y adaptaciones regulatorias. Se conserva el criterio de reutilización del responsable del proyecto.

[LICENSE](LICENSE) · [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) · [CONTRIBUTING.md](CONTRIBUTING.md).
