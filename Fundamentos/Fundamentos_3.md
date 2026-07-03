# ▶️ Iniciar un contenedor existente 

Inicia un contenedor que se encuentra detenido.

```bash
docker start <container-id|container-name>
```

> 💡 **Nota:** El contenedor conserva su estado y continúa desde el punto en que fue detenido.

---

# ⏹️ Detener un contenedor

Finaliza la ejecución de un contenedor de forma controlada.

```bash
docker stop <container-id|container-name>
```

> 📌 Docker envía inicialmente una señal **SIGTERM** para permitir que la aplicación finalice correctamente. Si el proceso no responde, posteriormente envía **SIGKILL**.

---

# 🗑️ Contenedores temporales

Un contenedor temporal se ejecuta utilizando la opción **`--rm`**, lo que indica que Docker eliminará automáticamente el contenedor una vez finalizada su ejecución.

```bash
docker run --rm alpine echo "Hola desde un contenedor temporal"
```

## 🔍 Explicación

| Parámetro | Descripción |
|-----------|-------------|
| `docker run` | Crea y ejecuta un contenedor. |
| `--rm` | Elimina automáticamente el contenedor al finalizar su ejecución. |
| `alpine` | Imagen oficial de Linux extremadamente ligera, ideal para pruebas. |
| `echo "Hola..."` | Comando que se ejecutará dentro del contenedor. |

> 💡 **Resultado:** Después de ejecutar el comando, el contenedor ya no aparecerá al listar los contenedores.

Comprobar:

```bash
docker ps -a
```

---

# 📜 Visualización de logs

Consulta los registros generados por un contenedor.

```bash
docker logs <container-id|container-name>
```

---

# 📡 Visualización de logs en tiempo real

Permite monitorear continuamente los registros del contenedor.

```bash
docker logs -tf <container-id|container-name>
```

## 🔍 Opciones

| Opción | Descripción |
|---------|-------------|
| `-f` ó `--follow` | Muestra los logs en tiempo real. |
| `-t` ó `--timestamps` | Agrega la fecha y hora a cada evento registrado. |

> 💡 Para finalizar la visualización utilice **Ctrl + C**.

---

# ❌ Eliminar un contenedor detenido

Elimina un contenedor que ya no se encuentra en ejecución.

```bash
docker container rm <container-id|container-name>
```

> ⚠️ El contenedor debe estar detenido antes de eliminarlo.

---

# 📊 Monitoreo de recursos

## docker stats

Muestra en tiempo real el consumo de recursos de uno o varios contenedores.

```bash
docker stats [opciones] [contenedor1 contenedor2 ...]
```

### 📈 Información mostrada

| Columna | Descripción |
|----------|-------------|
| 🆔 **CONTAINER ID** | Identificador único del contenedor. |
| 📦 **NAME** | Nombre asignado al contenedor. |
| ⚙️ **CPU %** | Porcentaje de CPU utilizado. |
| 🧠 **MEM USAGE / LIMIT** | Memoria utilizada y límite disponible. |
| 📉 **MEM %** | Porcentaje de memoria consumida. |
| 🌐 **NET I/O** | Tráfico de red recibido y enviado. |
| 💽 **BLOCK I/O** | Operaciones de lectura y escritura en disco. |
| 🔄 **PIDS** | Número de procesos o hilos en ejecución. |

### Opciones frecuentes

| Opción | Descripción |
|---------|-------------|
| `--no-stream` | Muestra las estadísticas una sola vez. |
| `--format` | Personaliza el formato de salida utilizando Go Templates. |

### 📌 Ejemplo

```bash
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

---

# 🔎 Inspeccionar un contenedor

Obtiene información detallada sobre la configuración y el estado del contenedor.

```bash
docker inspect <container-id|container-name>
```

> 📌 Permite consultar información relacionada con redes, volúmenes, variables de entorno, límites de recursos y configuración interna.

---

# 🖥️ Procesos en ejecución

Lista los procesos que se encuentran ejecutándose dentro de un contenedor.

```bash
docker top <container-id|container-name>
```

> 💡 Equivale al comando **ps** en sistemas Linux.

---

# 📢 Eventos del motor Docker

Monitorea en tiempo real los eventos generados por Docker.

```bash
docker events
```

Entre los eventos registrados se incluyen:

- ▶️ Inicio de contenedores.
- ⏹️ Detención de contenedores.
- 🗑️ Eliminación de contenedores.
- 🌐 Creación de redes.
- 💾 Gestión de volúmenes.

---

# 💾 Uso del almacenamiento

Consulta el espacio utilizado por imágenes, contenedores, volúmenes y caché.

```bash
docker system df
```

> 💡 Este comando resulta especialmente útil para identificar recursos que pueden eliminarse y liberar espacio en disco.
