# Publicar los archivos en GitHub

1. Descomprimir el ZIP de reemplazo. Los archivos están en la raíz del ZIP, sin carpeta contenedora adicional.
2. Copiar todo el contenido sobre la raíz de `ciso-assistant-bccr-sinpe`, conservando las rutas y reemplazando los archivos con el mismo nombre. Incluye `.github` y `.gitignore`, que macOS puede ocultar.
3. Para subir por la web: usar Add file → Upload files y cargar los archivos y carpetas descomprimidos. No subir únicamente el ZIP. Si `.github` queda fuera, reemplazar manualmente `.github/workflows/validate-scaffold.yml` con el archivo incluido.
4. Guardar el cambio y comprobar que Actions termina correctamente.
5. Crear una Release con etiqueta propuesta `v0.1.1`, adjuntando el YAML de `framework/releases/`. Se puede adjuntar también el ZIP de importación integral entregado anteriormente.

Este paquete no elimina archivos antiguos: si ya agregaste un YAML anterior, puedes conservarlo claramente identificado como histórico. El nuevo README apunta solo a la evaluación integral. No reemplazar archivos con datos propios de clientes o evaluaciones confidenciales.

La publicación en ARG INNOVA no envía automáticamente una contribución al proyecto de Intuitem; eso requiere otro Pull Request.
