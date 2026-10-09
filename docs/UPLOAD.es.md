# Cómo subir la estructura a GitHub

## Desde el ZIP

1. Descomprimir `ciso-assistant-bccr-sinpe-initial.zip`.
2. Abrir la carpeta `ciso-assistant-bccr-sinpe` incluida en el ZIP.
3. Subir **su contenido** a la raíz del repositorio GitHub `ciso-assistant-bccr-sinpe`. No subir el ZIP como sustituto de los archivos ni crear una carpeta adicional con el mismo nombre dentro del repositorio.
4. Incluir `.github/` y `.gitignore`. En Finder, `Cmd + Shift + .` permite ver elementos ocultos. Si la carga web omite elementos ocultos, usar Git o GitHub Desktop para copiarlos y publicarlos.
5. Si GitHub ya generó README, LICENSE o .gitignore, revisar y reemplazar esos archivos con las versiones de este paquete. Es esencial sustituir la licencia MIT genérica por la versión con alcance expreso del paquete.
6. Revisar el cambio y confirmar el commit. Comprobar que `README.md`, `LICENSE` y `.github/workflows/validate-scaffold.yml` estén en las rutas correctas.
7. Revisar la pestaña Actions. Si las políticas del repositorio requieren habilitar Actions, hacerlo antes de comprobar la ejecución. El nombre del workflow es “Validate repository scaffold (no framework validation)”.

## Si se trabaja con un clon existente

Copiar el contenido del paquete sobre el clon, sin borrar `.git/`. Revisar las diferencias antes de confirmar y publicar; conservar cualquier trabajo previo que corresponda. Ejecutar desde la raíz:

```sh
python3 scripts/validate_scaffold.py
```

El ZIP no incluye `.git/`, remotos configurados, credenciales ni una publicación automática. No hace falta crear manualmente las carpetas. Un workflow verde solo verifica la estructura inicial y no acredita validación normativa ni compatibilidad de importación.
