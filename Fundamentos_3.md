# ⚙️ Iniciar un contenedor ya existente

```bash
docker start <container-id>
```
---

# ⚙️ Detener un contenedor

```bash
docker stop <container-id>
```
---

# ⚙️ Contenedores temporales

Un contenedor temporal en Docker se ejecuta con la opción --rm. Esto significa que el contenedor se
eliminará automáticamente despuás de que finalice su ejecución, evitando que quede almacenado en su
sistema.

```bash
docker run --rm alpine echo "Hola desde un contenedor temporal"
```

>- docker run → ejecuta un contenedor.
>- --rm → indica que el contenedor se eliminará automáticamente al terminar.
>- alpine → imagen muy ligera de Linux (ideal para pruebas rápidas).
>- echo ”Hola desde un contenedor temporal” → comando que se ejecutará dentro del contenedor

Después de este comando, si ejecuta docker `ps -a`, no verá el contenedor porque ya fue
eliminado.

---

# ⚙️ Logs en contenedores

```bash
docker logs <container-id>
```
## Logs en contenedores en tiempo real

```bash
docker logs -tf <container-id>
```

>- -f ó --follow → hace que los logs se muestren en tiempo real.
>- -t ó --timestamps → Agrega la marca de tiempo a cada línea de log, mostrando cuando ocurrió cada evento.

Para salir de esta visulaización se debe usar Ctrl + C.


