# Importación y actualización de BCCR–SINPE v0.1.2

## Elegir la categoría

| Categoría | Archivo | Controles técnicos | Obligatorios | Opcionales | Checklist | Total evaluable | Versión YAML |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | [bccr-sinpe-nt-rcs-ed7-evaluacion-integral.yaml](../framework/releases/bccr-sinpe-nt-rcs-ed7-evaluacion-integral.yaml) | 47 | 43 | 4 | 66 | 113 | 3 |
| 2 | [bccr-sinpe-nt-rcs-ed7-evaluacion-integral-cat2.yaml](../framework/releases/bccr-sinpe-nt-rcs-ed7-evaluacion-integral-cat2.yaml) | 39 | 29 | 10 | 66 | 105 | 1 |

Cada biblioteca añade 9 notas no evaluables. Los 66 criterios procedimentales se agrupan en preparación (17), informe (36), seguimiento (6) e incidentes (7); no son controles oficiales adicionales.

1. Respalde su instancia y conserve auditorías, respuestas y evidencias existentes.
2. Descargue el YAML de la categoría de conexión correspondiente. Si descarga el ZIP, descomprímalo; no cargue el ZIP como biblioteca.
3. Cargue el YAML mediante Governance > Libraries > Add your own library y active la biblioteca si la instalación lo requiere.
4. Cree una evaluación nueva con la biblioteca de la categoría indicada. No hay grupos `cat1`, `cat2` ni grupos procedimentales que seleccionar. No combine ambas bibliotecas en la misma auditoría.
5. Confirme 113 preguntas en categoría 1 o 105 en categoría 2. Todas las técnicas ofrecen Cumple / No cumple; las procedimentales añaden No aplica. Justifique la ausencia de la condición o evento que lo permite. Una revisión pendiente, falta de evidencia o una obligación aplicable no justifican No aplica.
6. Registre evidencia y observaciones. Deje sin responder lo aún no evaluado. Compruebe los resultados en una evaluación de prueba antes de uso operativo.

## Evaluaciones anteriores

Categoría 1 conserva los URN de la biblioteca integral previa y sube la versión YAML a 3. Categoría 2 usa URN independientes y versión YAML 1. Esto no garantiza migración de respuestas, preguntas ni grupos seleccionados de auditorías antiguas. Cree evaluaciones nuevas y transfiera la evidencia con revisión del auditor; conserve las anteriores como historial. No borre auditorías para instalar esta revisión.

## Cumplimiento y puntuación

Las opciones calculan resultados con `compute_result`, sin `add_score`. Los campos de score se proponen ocultos; el rango 0–100 puede continuar visible como metadato en la ficha del framework. No representa una escala de madurez definida por NT-RCS. Los porcentajes de estados no constituyen un dictamen regulatorio ni compensan controles obligatorios incumplidos.

## Seguimiento de mitigaciones

Utilice los controles aplicados de la evaluación para registrar acciones y vincularlas con requisitos. Asigne responsable, prioridad y fecha objetivo; registre estado, avance y evidencia. Use el plan de acción y Kanban para seguimiento. El auditor debe verificar la corrección antes de cambiar el resultado del requisito. No se generan automáticamente responsables, plazos, acciones o notificaciones.

## English

Import the YAML for one connection category and create a new assessment. Category 1 contains 113 assessable requirements (47 technical + 66 procedural); category 2 contains 105 (39 + 66). There are no category/checklist group selections. Category 1 retains earlier integral URNs (YAML v3); category 2 has independent URNs (YAML v1). Existing assessment migration is not guaranteed. Preserve historical audits and evidence. All technical questions use Compliant / Noncompliant; procedural Not applicable requires justification. Native applied controls support mitigation tracking, but a full mitigation lifecycle has not yet been tested.

[Validation](VALIDATION.md) · [Sources](SOURCES.md) · [Traceability](TRACEABILITY.json)
