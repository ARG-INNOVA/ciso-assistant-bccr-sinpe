# BCCR–SINPE — evaluación integral

Preparado por **ARG INNOVA** — https://www.arginnova.com.
Fuente normativa: **Banco Central de Costa Rica**, NT-RCS edición 7, vigencia 11/02/2026.

## Importar

1. Descomprimir el ZIP y cargar `bccr-sinpe-nt-rcs-ed7-evaluacion-integral.yaml` mediante la función de carga/importación de bibliotecas de CISO Assistant. No cargar el ZIP como biblioteca.
2. Activar la biblioteca y crear una nueva evaluación con **BCCR–SINPE NT-RCS edición 7 — evaluación integral**. Esta biblioteca tiene URNs propias y no reemplaza automáticamente la anterior ni migra evaluaciones existentes. No importar ambas esperando una actualización en sitio.
3. Seleccionar **una sola categoría**: `cat1` muestra los 47 controles aplicables (43 obligatorios y 4 opcionales); `cat2` muestra 39 (29 obligatorios y 10 opcionales), excluyendo los 8 no aplicables. Los opcionales ya están incluidos: no existe un grupo opcional separado. Por defecto está seleccionado `cat1`. Al usar `cat2`, desmarcar `cat1`. La clasificación de ambas categorías aparece al inicio del texto de cada control.
4. Mantener seleccionados los cuatro grupos `checklist-preparation`, `checklist-report`, `checklist-followup` y `checklist-incidents` para conservar la evaluación integral. Están seleccionados por defecto. Si se desmarca una etapa, sus requisitos se excluyen de la selección; eso no significa cumplimiento ni exime de una obligación normativa.
5. Para los controles técnicos, registrar resultado y evidencias mediante las funciones de evaluación habituales. Para cada requisito del checklist, responder la pregunta **Resultado del checklist**.
6. Registrar evidencia, responsable y fecha en los campos disponibles o en los comentarios del requisito. Si se usa comentario: `Responsable: …; Fecha: …; Evidencia: …`. Estos datos no son campos adicionales inventados por el YAML y no se rellenan automáticamente.

La función de preguntas y `compute_result` debe estar soportada por la versión instalada. La referencia de implementación utilizada es el commit `de943807c3b5e0d5dd8e92ff39bfadbc950bd7f8` del proyecto oficial. No se ha ejecutado la carga en la instalación del usuario; los nombres exactos de menús pueden variar.

## Estructura

| Etapa | Elementos |
| --- | ---: |
| Preparación y requisitos previos | 17 checklist |
| Controles técnicos, sección 6 | 47 controles oficiales |
| Elaboración y presentación del informe | 36 checklist |
| Seguimiento y atención de observaciones | 6 checklist |
| Incidentes, recertificación y reconexión | 7 checklist |
| Definiciones y contexto regulatorio | 9 notas no evaluables |

Son **66 criterios de checklist y 47 controles técnicos**, no 113 controles oficiales del BCCR. El avance total de CISO Assistant puede incluir el checklist: no debe confundirse con el cumplimiento de los 47 controles técnicos ni con el dictamen del BCCR.

## Resultados sin puntuación numérica

Las preguntas del checklist permiten **Cumple / No cumple**. Solo las obligaciones condicionadas incluyen **No aplica**, con la condición escrita en el requisito. Sin respuesta, el requisito permanece sin evaluar. No usar No aplica solo porque una revisión o etapa aún esté pendiente.

Las opciones usan `compute_result` y no tienen `add_score`: cambian el estado de cumplimiento sin generar puntuación numérica. Los campos de puntuación y puntuación documental se proponen ocultos en las nuevas evaluaciones, para trabajar con resultados y evidencias. No se usa peso cero, que no garantiza exclusión en los cálculos de la aplicación. Si una instalación cambia esa configuración o permite introducir puntajes manuales, deberá mantener el checklist sin puntuación.

**El incumplimiento de un requisito previo o del informe puede invalidar el proceso aunque no produzca puntaje.** No se configura un dictamen regulatorio automático. Según 5.2.1, cualquier control obligatorio no satisfecho adecuadamente implica incumplimiento del informe completo; un promedio o porcentaje no sustituye esta regla.

## Numeración y trazabilidad

Los controles técnicos conservan sus números y nombres oficiales. Los requisitos procedimentales utilizan la sección de origen y letras: por ejemplo, `5.4.3.A` para remisión mediante caso, `5.4.3.B` para el oficio firmado y `5.4.3.C` para la revisión de forma y fondo. **Los sufijos son desgloses editoriales de ARG INNOVA; no aparecen en la norma.**

El anexo tiene encabezados sin subnumeración: se utilizan `7.A`, `7.B`, etc., indicando el encabezado original en la referencia de cada requisito. Las etiquetas de etapa son agrupaciones editoriales.

[TRACEABILITY.json](TRACEABILITY.json) registra el contenido ES/EN, sección, páginas, condición, tipo y correspondencia con los 42 registros anteriores. Esos registros se desglosaron en 75 entradas: 66 checklist y 9 notas. No se perdió ninguno de los 42 registros. Las definiciones, vigencias, potestades sancionatorias, anexos adicionales permitidos y actividad de actualización del BCCR permanecen como contexto, sin crear obligaciones para la entidad.

## Validación y créditos

Se conservaron íntegramente los textos de los 47 controles y sus traducciones, así como categorías, alcances y excepciones. Se comprobó la estructura YAML, URNs, padres, idiomas y cobertura de los 42 registros anteriores. El método oficial de almacenamiento se ejecutó en modo dry-run con consulta de biblioteca cargada simulada. Se probó la lógica oficial de respuestas con datos en memoria en **230 casos**, incluidos resultados positivos, negativos, no aplicables y sin respuesta; todos conservaron `score=None` e `is_scored=False`. Estas comprobaciones no equivalen a una importación real en base de datos. Detalles en [VALIDATION_RESULTS.json](VALIDATION_RESULTS.json).

El español de los controles es transcripción de la norma; el checklist contiene síntesis y desgloses editoriales. Inglés: traducción no oficial. Prevalece el PDF del BCCR: https://www.bccr.fi.cr/content/dam/bccr/publicaciones/sistemas-de-pagos/nt-requisitos-ciberseguridad-para-participar-sinpe.pdf.

Autoridad normativa: BCCR. Preparación y traducción no oficial: ARG INNOVA. Información comercial y servicios opcionales: https://www.arginnova.com. No implica aval BCCR o Intuitem ni exige contratar servicios. La reutilización sigue el criterio y autorización comunicados por el responsable del proyecto. La licencia MIT adjunta cubre únicamente contenido original autorizado; excluye texto BCCR, traducciones y adaptaciones regulatorias. No se incluye el PDF oficial. La revisión externa es opcional, no requisito para continuar.

## Para el repositorio GitHub

Guardar el YAML nuevo en `framework/releases/` y estas instrucciones y la trazabilidad en `docs/`. No reemplazar los README generales con este documento ni subir solo el ZIP como si fuese la biblioteca.

## English

Import the YAML, activate the library and create a **new comprehensive assessment**. It uses separate URNs and does not migrate or automatically replace previous assessments. Select all applicable technical controls from **one category only** (`cat1` or `cat2`, both include optional controls), and retain the four procedural checklist stage groups. There are 47 official technical controls, 66 editorial checklist criteria and 9 non-assessable context notes. Checklist answers drive Compliant/Noncompliant status without numeric scores; conditional requirements also offer Not applicable. Leave unreviewed or future-stage items unassessed. Record evidence, responsible person and date through available fields or comments. Numeric score fields are proposed hidden in new assessments. Overall application progress may include checklists; it is not the regulatory verdict for the 47 technical controls. Letter suffixes are editorial subdivisions, not BCCR numbering. English is unofficial; the Spanish PDF prevails. Native result logic was tested in 230 in-memory cases; an actual database import in the user installation remains untested. ARG INNOVA: https://www.arginnova.com.

## Actualización de opcionales

Biblioteca YAML versión 2. Reimportar y crear una evaluación nueva o usar la actualización de biblioteca/framework disponible en la instalación. Las evaluaciones existentes pueden conservar selecciones o referencias anteriores; no se afirma migración automática. Seleccionar `cat1` o `cat2`. 6.3.3 aparece en ambas y muestra Opcional para las dos categorías.
