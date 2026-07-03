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


# ⚙️ Borrar un contenedor detenido

```bash
docker container rm <container-id>
```


# ⚙️ Estadísticas en Docker

## docker stats

Este comando muestra estadísticas en tiempo real del uso de recursos de los contenedores, como CPU,
memoria, red y disco.


```bash
docker stats [opciones] [contenedor1 contenedor2 ...}
```

| Columna | Significado |
|----------|-------------|
| **CONTAINER ID** | Identificador único del contenedor. |
| **NAME** | Nombre asignado al contenedor. |
| **CPU %** | Porcentaje de CPU utilizado por el contenedor. |
| **MEM USAGE / LIMIT** | Cantidad de memoria utilizada y límite de memoria asignado al contenedor. |
| **MEM %** | Porcentaje de memoria utilizada con respecto al límite disponible. |
| **NET I/O** | Tráfico de red del contenedor (datos recibidos y enviados). |
| **BLOCK I/O** | Operaciones de entrada y salida en disco (lectura y escritura). |
| **PIDS** | Número de procesos o hilos que se encuentran en ejecución dentro del contenedor. |

>- --no-stream → Muestra las estad´ısticas una sola vez en vez de en tiempo real.
>- --format → Permite personalizar la salida usando Go templates, por ejemplo:

```bash
docker stats -- format " table {{.Name }}\ t {{.CPUPerc }}\ t {{.MemUsage }} 
```
