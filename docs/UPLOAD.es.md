# Publicación del paquete v0.1.2

Mantener sincronizados los dos YAML de framework/releases, los README ES/EN, CHANGELOG.md, framework/metadata.json y la documentación de importación y validación. Ejecutar la validación automática antes de publicar.

Crear la etiqueta v0.1.2 sobre el commit que contiene esos cambios y adjuntar los dos YAML, el ZIP y sus sumas SHA-256. El ZIP contiene ambas bibliotecas, guía, licencia y validación. No sustituir los archivos históricos del release v0.1.1.

Las notas deben indicar que la aceptación en CISO Assistant sigue pendiente y que se probaron ambas importaciones y resultados; el ciclo completo de mitigación aún no está probado. No publicar datos identificables de auditorías, capturas de clientes ni direcciones de instancias.

Actualizar la validación del PR existente sin afirmar aceptación o fusión. [Estado del proyecto](PROJECT_STATUS.md).
