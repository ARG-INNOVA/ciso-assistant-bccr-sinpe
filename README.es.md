# BCCR–SINPE para CISO Assistant

Estructura inicial mantenida por **ARG INNOVA** para preparar una biblioteca de cumplimiento de ciberseguridad BCCR–SINPE de Costa Rica para CISO Assistant.

**Estado: preparación inicial.** No incluye un Excel final, un YAML de framework importable, un inventario de controles verificados ni mapeos completados. No se afirma que existan 47 controles verificados. Están pendientes la selección y revisión de documentos normativos, versiones, fechas de vigencia y alcance. La compatibilidad con CISO Assistant no ha sido probada.

[English](README.md)

## Propósito y alcance

Preparar una representación trazable y revisada de los requisitos BCCR–SINPE aplicables. Antes de redactar controles, se deben determinar la aplicabilidad, las versiones de las fuentes y los límites de cada requisito. Es una iniciativa comunitaria independiente; no se afirma afiliación ni aval del BCCR o de Intuitem. Esta estructura no acredita cumplimiento ni constituye asesoría jurídica.

## Estructura

- `framework/`: estado y espacios para borradores y futuras entregas revisadas.
- `docs/`: fuentes, licencia, validación, importación y publicación.
- `mappings/`: metodología y plantilla vacía de mapeo.
- `scripts/`: comprobación estructural sin dependencias externas.
- `.github/workflows/`: workflow funcional de comprobación de la estructura.
- `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE` y `THIRD_PARTY_NOTICES.md`: colaboración, historial y condiciones de uso.

## Inicio

1. Consultar el [estado del proyecto](docs/PROJECT_STATUS.md) y el [registro de fuentes](docs/SOURCES.md).
2. Seguir las [instrucciones de carga](docs/UPLOAD.es.md).
3. Ejecutar `python3 scripts/validate_scaffold.py` desde la raíz del repositorio (Python 3.9 o superior).
4. Completar la revisión normativa y la [lista de validación](docs/VALIDATION.md) antes de generar una entrega del framework.

El workflow se ejecuta en pushes y pull requests y permite ejecución manual. Un resultado satisfactorio confirma únicamente la estructura; no valida requisitos normativos, esquemas Excel/YAML, mapeos ni importación.

## Importación

**Todavía no hay archivos para importar.** Consultar el [plan de importación](docs/IMPORT.md). Antes de producir Excel o YAML, registrar una versión o commit de CISO Assistant y comprobar el formato documentado para esa versión. No cambiar las extensiones de los placeholders para simular archivos importables.

## Licencia y colaboración

La [licencia MIT](LICENSE) cubre únicamente contenido original cuyos titulares autoricen esa licencia. Quedan excluidos los reglamentos, publicaciones, citas, logotipos y demás material del BCCR o de terceros. El repositorio no concede derechos sobre ese material. Ver la [política de licencia](docs/LICENSING.md), los [avisos de terceros](THIRD_PARTY_NOTICES.md) y la [guía de contribución](CONTRIBUTING.md).

## Referencias oficiales

- [Banco Central de Costa Rica](https://www.bccr.fi.cr/): punto inicial de búsqueda, no una base normativa ya seleccionada.
- [Repositorio de CISO Assistant](https://github.com/intuitem/ciso-assistant-community): verificar formatos y requisitos de contribución contra la versión elegida.

Estos enlaces no implican validación normativa ni aceptación del proyecto upstream.
