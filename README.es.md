# BCCR–SINPE para CISO Assistant

Preparado y mantenido por **[ARG INNOVA](https://www.arginnova.com)**. [English](README.md).

Biblioteca de evaluación integral basada en la NT-RCS del Banco Central de Costa Rica, edición 7, con vigencia del 11 de febrero de 2026.

| Contenido | Cantidad |
| --- | ---: |
| Controles técnicos oficiales | 47 |
| Criterios procedimentales de checklist | 66 |
| Notas de contexto no evaluables | 9 |

Los 66 criterios son desgloses editoriales de obligaciones y requisitos procedimentales; no son controles oficiales adicionales. Los checklist se agrupan en preparación (17), elaboración y presentación del informe (36), seguimiento (6) e incidentes y reconexión (7).

## Descargar e importar

- [YAML — biblioteca de evaluación integral](framework/releases/bccr-sinpe-nt-rcs-ed7-evaluacion-integral.yaml)
- [Instrucciones de importación](docs/IMPORT.md)
- [Versiones y descargas](https://github.com/ARG-INNOVA/ciso-assistant-bccr-sinpe/releases)

Importar el YAML mediante la función de carga de bibliotecas de CISO Assistant y crear una evaluación nueva. Usar los grupos técnicos de una sola categoría; mantener los cuatro grupos del checklist. Esta biblioteca tiene URNs propias y no migra automáticamente evaluaciones anteriores.

Categoría 1 muestra 47 controles (43 obligatorios y 4 opcionales). Categoría 2 muestra 39 (29 obligatorios y 10 opcionales); excluye 8 no aplicables. Por defecto se selecciona categoría 1 completa y los cuatro checklist. La clasificación de ambas categorías aparece al inicio de cada control.

El checklist utiliza Cumple / No cumple y, en requisitos condicionados, No aplica. Sus respuestas cambian el estado sin generar puntuación numérica. Los campos de puntuación se proponen ocultos en nuevas evaluaciones. El avance global puede incluir checklist y no equivale al dictamen regulatorio del BCCR.

## Idiomas, referencias y validación

Los controles técnicos conservan texto español e IDs oficiales. Inglés: traducción no oficial; prevalece el PDF español. Los sufijos como 5.4.3.A y 7.A son desgloses de ARG INNOVA, no numeración del BCCR.

El usuario reportó importación y revisión visual satisfactorias. Se realizaron comprobaciones de estructura, texto y aplicabilidad, y 230 casos con la lógica oficial de respuestas usando datos en memoria. No se ejecutó una prueba aislada de importación en base de datos; la versión de la instalación del usuario no fue registrada.

- [Fuente normativa](docs/SOURCES.md)
- [Alcance de validación](docs/VALIDATION.md)
- [Resultados de las pruebas](docs/VALIDATION_RESULTS.json)
- [Trazabilidad de desgloses](docs/TRACEABILITY.json)
- [Estado del proyecto](docs/PROJECT_STATUS.md)

## ARG INNOVA

Para información de la empresa y servicios profesionales opcionales, visitar [www.arginnova.com](https://www.arginnova.com).

Los créditos corresponden a la preparación de la biblioteca y traducción no oficial; la norma pertenece al BCCR. No se afirma aval del BCCR o Intuitem. El uso del contenido abierto autorizado no requiere contratar servicios.

## Licencia y contribuciones

MIT cubre únicamente contenido original autorizado. Texto BCCR, traducciones y adaptaciones normativas quedan excluidos de la concesión. La reutilización normativa se realiza conforme al criterio y autorización del responsable del proyecto.

[LICENSE](LICENSE) · [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) · [CONTRIBUTING.md](CONTRIBUTING.md).

La publicación en este repositorio es independiente de una eventual aceptación en el proyecto oficial de CISO Assistant.
