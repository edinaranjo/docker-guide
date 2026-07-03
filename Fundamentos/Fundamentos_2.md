# 🚀 Creación de contenedores

Crea un nuevo contenedor a partir de una imagen Docker. 

```bash
docker run -it --name <container-name> \
-p <host-port>:<container-port> \
-d <image-name>
```

> 💡 **Nota:** Este comando permite asignar un nombre al contenedor, publicar puertos y ejecutarlo en segundo plano.

---

# 🖥️ Ejecución en modo interactivo

Permite iniciar un contenedor y acceder directamente a su terminal.

```bash
docker run -it <image-name>
```

> 📌 Ideal para realizar pruebas, instalar paquetes o explorar el sistema de archivos del contenedor.

---

# ⚡ Ejecución en segundo plano

Ejecuta un contenedor como servicio (*Detached Mode*).

```bash
docker run -d <image-name>
```

## 📌 Ejemplo

```bash
docker run -d --name miweb -p 8080:80 nginx
```

### 🔍 Explicación

| Parámetro | Descripción |
|-----------|-------------|
| `docker run` | Crea y ejecuta un nuevo contenedor. |
| `-d` | Ejecuta el contenedor en segundo plano (*Detached Mode*). |
| `--name miweb` | Asigna el nombre **miweb** al contenedor. |
| `-p 8080:80` | Publica el puerto 80 del contenedor en el puerto 8080 del host. |
| `nginx` | Utiliza la imagen oficial de Nginx. |

---

# 💻 Acceso a un contenedor

Permite ejecutar comandos dentro de un contenedor en ejecución.

```bash
docker exec -it <container-name|container-id> <command>
```

## 📌 Ejemplo

```bash
docker exec -it miweb bash
```

> 💡 Si la imagen no dispone de **bash**, utiliza:

```bash
docker exec -it miweb sh
```

---

# ❤️ Configuración de Healthcheck

El *Healthcheck* permite comprobar automáticamente si un servicio continúa funcionando correctamente.

```bash
docker run -d \
--name miweb \
-p 8080:80 \
--health-cmd="curl -f http://localhost/ || exit 1" \
--health-interval=30s \
--health-retries=3 \
nginx
```

## 🔍 Parámetros

| Parámetro | Descripción |
|-----------|-------------|
| `--health-cmd` | Comando utilizado para verificar el estado del servicio. |
| `--health-interval=30s` | Intervalo entre cada verificación. |
| `--health-retries=3` | Número máximo de intentos antes de marcar el contenedor como **unhealthy**. |

---

# 🔎 Verificar el estado del Healthcheck

Consulta el estado actual del Healthcheck configurado en un contenedor.

```bash
docker inspect --format='{{json .State.Health.Status}}' <container-name>
```

## 📊 Posibles estados

| Estado | Descripción |
|---------|-------------|
| 🟢 **healthy** | El contenedor funciona correctamente. |
| 🟡 **starting** | El Healthcheck aún se encuentra inicializando. |
| 🔴 **unhealthy** | El Healthcheck ha detectado fallos en el servicio. |

> 💡 **Recomendación:** Utiliza siempre **Healthcheck** en aplicaciones que ejecuten servicios web, APIs o bases de datos. Esto permite que Docker detecte automáticamente fallos operacionales y facilita la integración con herramientas de orquestación como Docker Compose, Docker Swarm y Kubernetes.
