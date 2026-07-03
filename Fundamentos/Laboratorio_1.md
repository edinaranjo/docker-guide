# 🐳 Laboratorio: Administración Básica de Contenedores con HashiCorp Http-Echo


## Objetivos

Al finalizar esta práctica el estudiante será capaz de:

>- Crear un contenedor Docker a partir de una imagen oficial.

>- Publicar un servicio HTTP mediante Docker.

>- Consultar el estado de los contenedores.

>- Analizar los registros generados por una aplicación.

>- Inspeccionar la configuración interna de un contenedor.

>- Monitorear el consumo de recursos.

>- Detener y eliminar contenedores.

---

## Escenario

En este laboratorio se desplegará un pequeño servidor HTTP basado en la imagen oficial HashiCorp Http-Echo, el cual responderá siempre con un mensaje personalizado.

Posteriormente se realizarán diferentes tareas administrativas para analizar el comportamiento del contenedor.

---
## Arquitectura del laboratorio

                    Navegador Web
                           │
                    http://localhost:5678
                           │
                           ▼
              +-----------------------------+
              |  HashiCorp Http-Echo        |
              |     Docker Container        |
              +-----------------------------+
                     │      │       │
                     │      │       │
                     ▼      ▼       ▼
              docker logs  docker exec
                     │
                     ▼
              docker top
                     │
                     ▼
              docker inspect
                     │
                     ▼
              docker stats
                     │
                     ▼
                Healthcheck

---
## Descarga de la imagen

### 1. Consulte las imágenes disponibles

```bash
docker image ls
```

### 2. Descargar la imagen

```bash
docker pull hashicorp/http-echo
```

### 3. Verificar

```bash
docker image ls
```

  Debe aparecer

```bash
IMAGE                        ID             DISK USAGE   CONTENT SIZE   EXTRA
hashicorp/http-echo:latest   fcb75f691c8b       16.7MB         4.63MB 
```
---

## Crear el contenedor con Healthcheck

```bash
docker run -d \
--name echo-lab \
-p 5678:5678 \
--health-cmd="wget --spider -q http://localhost:5678 || exit 1" \
--health-interval=20s \
--health-timeout=5s \
--health-retries=3 \
--health-start-period=10s \
hashicorp/http-echo \
-text="Bienvenido al laboratorio Docker"
```
Explicación:

| Parámetro             | Descripción                             |
| --------------------- | --------------------------------------- |
| `-d`                  | Ejecuta el contenedor en segundo plano. |
| `--name`              | Asigna un nombre al contenedor.         |
| `-p 5678:5678`        | Publica el puerto HTTP.                 |
| `--health-cmd`        | Verifica que el servicio HTTP responda. |
| `--health-interval`   | Frecuencia de comprobación.             |
| `hashicorp/http-echo` | Imagen utilizada.                       |
| `-text`               | Mensaje que devolverá el servidor HTTP. |

---

## Verificar el funcionamiento

### 1. Digitar la siguiente url en el navegador web

```bash
http://localhost:5678
```
Debe aparecer 

```bash
Bienvenido al laboratorio Docker
```
