
# 🐳 Laboratorio 2
# 📊 Monitoreo y Validación Operacional de Contenedores con Caddy Alpine

## 🎯 Objetivos

Al finalizar esta práctica el estudiante será capaz de:

- 🚀 Desplegar una aplicación real utilizando Docker.
- ❤️ Configurar e interpretar un **Healthcheck**.
- 📊 Analizar el estado operacional de un contenedor.
- ⚙️ Monitorear el consumo de recursos mediante `docker stats`.
- 🔍 Inspeccionar la configuración interna y los procesos del contenedor.
- 🌐 Realizar pruebas de conectividad HTTP para validar la disponibilidad del servicio.

---

# 📖 Escenario

En este laboratorio se desplegará una instancia de **Caddy Alpine** dentro de un contenedor Docker. Posteriormente se verificará el estado de salud del servicio mediante un **Healthcheck**, se realizarán pruebas de conectividad HTTP y se analizará el comportamiento del contenedor utilizando las principales herramientas de monitoreo y administración proporcionadas por Docker.

Este laboratorio representa un escenario típico utilizado por equipos **DevOps** para validar la disponibilidad de aplicaciones antes de su despliegue en ambientes productivos.

# 🏗️ Arquitectura del laboratorio 

```text
                           👨‍💻 Cliente
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          │                Navegador               curl
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │
                         http://localhost:8080
                                │
                                ▼
                 +----------------------------------+
                 |       🌐 Caddy Web Server        |
                 |                                  |
                 |        Docker Container          |
                 +----------------------------------+
                     │         │           │
                     │         │           │
                     ▼         ▼           ▼
               ❤️ Healthcheck  📊 Stats   🔍 Inspect
                     │
                     ▼
                 📜 Docker Logs
```

> 💡 **Objetivo del laboratorio:** Validar el estado operacional de un servidor web contenerizado mediante pruebas de disponibilidad, monitoreo de recursos y análisis de la configuración interna del contenedor.

---

# 📥 Paso 1. Descargar la imagen

En esta primera actividad se descargará la imagen oficial de **Caddy Alpine** desde **Docker Hub**. Posteriormente, se verificará que la imagen se encuentre disponible en el repositorio local del equipo.

```bash
docker pull caddy:alpine
```

Verificar que la imagen fue descargada correctamente.

```bash
docker image ls
```

Resultado esperado:

```text
REPOSITORY      TAG        IMAGE ID

caddy           alpine     xxxxxxxxxxxx
```

---

# 🚀 Paso 2. Crear el contenedor con Healthcheck

Crear un contenedor denominado **caddy-lab** configurando un **Healthcheck** que verifique periódicamente la disponibilidad del servidor web.

```bash
docker run -d \
--name caddy-lab \
-p 8080:80 \
--health-cmd="wget -q --spider http://127.0.0.1:80 || exit 1" \
--health-interval=10s \
--health-timeout=5s \
--health-retries=3 \
--health-start-period=10s \
caddy:alpine
```

### 🔍 Explicación de los parámetros

| Parámetro | Descripción |
|-----------|-------------|
| `docker run` | Crea y ejecuta un nuevo contenedor. |
| `-d` | Ejecuta el contenedor en segundo plano (*Detached Mode*). |
| `--name caddy-lab` | Asigna el nombre **caddy-lab** al contenedor. |
| `-p 8080:80` | Publica el puerto **80** del contenedor en el puerto **8080** del equipo anfitrión. |
| `--health-cmd` | Ejecuta una comprobación HTTP sobre la página principal del servidor web. |
| `--health-interval=10s` | Ejecuta el Healthcheck cada 10 segundos. |
| `--health-timeout=5s` | Tiempo máximo permitido para responder al Healthcheck. |
| `--health-retries=3` | Número de fallos consecutivos antes de marcar el contenedor como **unhealthy**. |
| `--health-start-period=10s` | Tiempo de espera antes de iniciar las comprobaciones del Healthcheck. |
| `caddy:alpine` | Imagen oficial de Caddy basada en Alpine Linux. |

> 💡 **Nota:** Caddy inicia el servidor web prácticamente de forma inmediata, por lo que un **Healthcheck** configurado con un período de espera corto resulta suficiente para verificar correctamente la disponibilidad del servicio.
---

# ❤️ Paso 3. Verificar el estado del contenedor

Consultar los contenedores en ejecución.

```bash
docker ps
```

Espere aproximadamente **40 a 60 segundos** hasta que Grafana complete su proceso de inicialización.

### 📌 Resultado esperado

```text
STATUS

Up 1 minute (healthy)
```

> 💡 La etiqueta **(healthy)** indica que el Healthcheck se ejecutó correctamente y que Docker considera que el servicio se encuentra operativo.

---

# 🔍 Paso 4. Analizar el Healthcheck

Consultar únicamente el estado actual del Healthcheck.

```bash
docker inspect \
--format='{{.State.Health.Status}}' \
caddy-lab
```

### 📌 Resultado esperado

```text
healthy
```

---

## 📊 Consultar el historial del Healthcheck

Mostrar el historial completo de las verificaciones realizadas por Docker.

```bash
docker inspect \
--format='{{json .State.Health}}' \
caddy-lab
```

Analice la información obtenida e identifique los siguientes elementos:

| Campo | Descripción |
|--------|-------------|
| **Status** | Estado actual del Healthcheck (`healthy` o `unhealthy`). |
| **ExitCode** | Código devuelto por el comando ejecutado durante la verificación. Un valor **0** indica éxito. |
| **FailingStreak** | Número de verificaciones consecutivas que han fallado. |
| **Log** | Historial completo de las comprobaciones realizadas, incluyendo fecha, hora y resultado de cada una. |

> 💡 **Pregunta de análisis:** ¿Por qué Docker no considera suficiente que el contenedor esté en estado **Up** y además ejecuta un **Healthcheck** para determinar si el servicio realmente se encuentra disponible?

---

---

# 🌐 Paso 5. Acceder al servidor web

Una vez iniciado el contenedor, abra un navegador web y acceda a la siguiente dirección:

```text
http://localhost:8080
```

Deberá visualizar la página predeterminada del servidor **Caddy**.

> 💡 **Nota:** La visualización de esta página confirma que el servidor web se encuentra operativo y que el puerto **8080** ha sido publicado correctamente en el equipo anfitrión.

---

# 🌍 Paso 6. Verificar la conectividad HTTP

Además del navegador, es posible comprobar la disponibilidad del servicio utilizando herramientas de línea de comandos.

## 📡 Consultar la página principal

Ejecute el siguiente comando desde una nueva terminal.

```bash
curl http://localhost:8080
```

### 📌 Resultado esperado

Se mostrará el contenido HTML correspondiente a la página predeterminada del servidor **Caddy**.

---

## 🔍 Verificar el código de respuesta HTTP

Consultar únicamente las cabeceras HTTP del servidor.

```bash
curl -I http://localhost:8080
```

### 📌 Resultado esperado

```text
HTTP/1.1 200 OK
```

### 🔍 Interpretación

| Código | Significado |
|----------|-------------|
| **200 OK** | El servidor procesó correctamente la solicitud HTTP y el servicio se encuentra disponible. |

> 💡 **Nota:** A diferencia de Grafana, Caddy responde directamente con un código **200 OK**, ya que sirve contenido web estático sin realizar redirecciones.

---

## 🌐 Comprobar conectividad mediante Ping

Si el protocolo ICMP se encuentra habilitado en el equipo anfitrión, ejecutar:

```bash
ping localhost
```

Interrumpir la ejecución utilizando:

```text
Ctrl + C
```

> 💡 Esta prueba permite comprobar únicamente la conectividad con el equipo anfitrión, no el funcionamiento del servidor web.

---

# 📈 Paso 7. Generar tráfico sobre el servidor

Con el objetivo de observar el comportamiento del contenedor bajo carga, genere múltiples solicitudes HTTP hacia el servidor.

Abra una nueva terminal y ejecute:

```bash
docker stats
```

Posteriormente, desde otra terminal, ejecute varias solicitudes consecutivas.

## Opción 1. Utilizando curl

```bash
for i in {1..50}
do
    curl http://localhost:8080 > /dev/null
done
```

---

## Opción 2. Utilizando ApacheBench (Recomendado)

Si ApacheBench se encuentra instalado:

```bash
ab -n 500 -c 20 http://localhost:8080/
```

Donde:

| Parámetro | Descripción |
|-----------|-------------|
| `-n 500` | Envía un total de 500 solicitudes HTTP. |
| `-c 20` | Mantiene 20 conexiones concurrentes. |

---

## 📊 Analizar las métricas de Docker

Mientras se generan las solicitudes, observe la salida del siguiente comando:

```bash
docker stats
```

Analice las siguientes métricas.

| Métrica | Descripción |
|----------|-------------|
| ⚙️ **CPU %** | Porcentaje de utilización del procesador. |
| 🧠 **MEM USAGE** | Memoria consumida por el contenedor. |
| 🌐 **NET I/O** | Cantidad de datos recibidos y transmitidos. |
| 🔄 **PIDS** | Número de procesos activos dentro del contenedor. |

> 💡 **Pregunta de análisis:** ¿Qué métrica presentó la mayor variación durante la generación de tráfico HTTP? ¿Por qué considera que dicho recurso fue el más afectado?

---

## 📌 Actividad adicional

Mientras continúa ejecutándose `docker stats`, abra varias pestañas del navegador y actualice continuamente la página principal del servidor.

Compare el consumo de recursos obtenido mediante el navegador con el observado durante la prueba automatizada realizada con **ApacheBench** o mediante múltiples solicitudes con **curl**.

Analice cuál de los dos métodos genera una mayor carga sobre el servidor web.


# 🔍 Paso 8. Inspeccionar el contenedor

Consultar la configuración completa del contenedor.

```bash
docker inspect caddy-lab
```

Analice la salida en formato **JSON** e identifique la siguiente información:

- 🌐 Dirección IP.
- 🖼️ Imagen utilizada.
- 🌍 Redes Docker configuradas.
- 🔌 Puertos publicados.
- ⚙️ Variables de entorno.
- ❤️ Configuración del Healthcheck.

---

## 📌 Consultar únicamente la dirección IP

```bash
docker inspect \
-f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
caddy-lab
```

### 💡 Pregunta de análisis

¿Por qué Docker asigna una dirección IP privada al contenedor si el servicio ya se encuentra publicado mediante el puerto **8080**?

---

# 🖥️ Paso 9. Analizar los procesos del contenedor

Consultar los procesos que actualmente se encuentran ejecutándose dentro del contenedor.

```bash
docker top caddy-lab
```

## 📊 Analizar la salida

Identifique la siguiente información:

| Campo | Descripción |
|--------|-------------|
| **PID** | Identificador del proceso dentro del sistema operativo. |
| **USER** | Usuario propietario del proceso. |
| **TIME** | Tiempo de CPU consumido. |
| **COMMAND** | Aplicación que se encuentra ejecutándose. |

> 💡 **Pregunta de análisis:** ¿Cuál considera que es el proceso principal del contenedor y por qué Docker necesita mantenerlo en ejecución para que el contenedor permanezca activo?

---


# 📜 Paso 10. Analizar los registros del contenedor

Los registros (*logs*) permiten conocer los eventos generados por una aplicación durante su ejecución. Son una herramienta fundamental para el diagnóstico de errores y el monitoreo operativo de servicios contenerizados.

Para visualizar los registros en tiempo real, ejecute:

```bash
docker logs -tf caddy-lab
```

## 🔍 Opciones utilizadas

| Opción | Descripción |
|---------|-------------|
| `-t` | Muestra la fecha y hora de cada evento registrado. |
| `-f` | Mantiene la visualización de los registros en tiempo real (*Follow Mode*). |

---
## 📈 Generar actividad sobre el servidor web

Mientras el comando permanece ejecutándose, genere múltiples solicitudes HTTP hacia el servidor.

Puede hacerlo de cualquiera de las siguientes maneras:

- 🌐 Actualizando repetidamente la página `http://localhost:8080`.
- 💻 Ejecutando varias solicitudes mediante `curl`.
- 🚀 Utilizando una herramienta de pruebas de carga como **ApacheBench (ab)**.

Observe cómo aparecen nuevos registros cada vez que el servidor recibe una solicitud HTTP.

> 💡 **Nota:** Para finalizar la visualización de los registros utilice la combinación de teclas **Ctrl + C**.

---

# ❤️ Paso 11. Simular un fallo del Healthcheck

En esta actividad se desplegará un segundo contenedor con un **Healthcheck** configurado deliberadamente de forma incorrecta. El objetivo es comparar un servicio **operativo (healthy)** con otro cuyo **Healthcheck** falla (**unhealthy**).

Crear el segundo contenedor.

```bash
docker run -d \
--name caddy-error \
-p 8081:80 \
--health-cmd="wget -q --spider http://127.0.0.1:9999 || exit 1" \
--health-interval=10s \
--health-timeout=5s \
--health-retries=2 \
--health-start-period=10s \
caddy:alpine
```

> 💡 **¿Qué ocurre en este ejemplo?**
>
> El servidor web continúa ejecutándose sobre el puerto **80**, sin embargo el Healthcheck intenta verificar el puerto **9999**, donde no existe ningún servicio. Como consecuencia, todas las comprobaciones fallarán y Docker marcará el contenedor como **unhealthy**.

Espere aproximadamente **30 segundos** para que Docker ejecute varias verificaciones.

---

## 📊 Comparar el estado de ambos contenedores

Consultar los contenedores en ejecución.

```bash
docker ps
```

### 📌 Resultado esperado

| Contenedor | Estado esperado |
|------------|----------------|
| 🟢 **caddy-lab** | `Up (healthy)` |
| 🔴 **caddy-error** | `Up (unhealthy)` |

Observe que ambos contenedores permanecen en ejecución, pero únicamente uno supera correctamente el Healthcheck.

---

## 🔍 Consultar el estado del Healthcheck

Verificar únicamente el estado del contenedor con error.

```bash
docker inspect \
--format='{{.State.Health.Status}}' \
caddy-error
```

### 📌 Resultado esperado

```text
unhealthy
```

También puede consultar el historial completo del Healthcheck.

```bash
docker inspect \
--format='{{json .State.Health}}' \
caddy-error
```

Analice los siguientes campos:

| Campo | Descripción |
|--------|-------------|
| **Status** | Estado actual del Healthcheck. |
| **FailingStreak** | Número de comprobaciones consecutivas que han fallado. |
| **Log** | Historial de las verificaciones realizadas por Docker. |

---

## 💡 Preguntas de análisis

1. ¿Por qué el contenedor **caddy-error** continúa en ejecución aunque Docker lo marque como **unhealthy**?
2. ¿Qué diferencia existe entre el estado **Up** mostrado por `docker ps` y el estado del **Healthcheck**?
3. ¿Qué ventajas ofrece un Healthcheck para plataformas como Docker Compose, Docker Swarm o Kubernetes?
4. ¿Qué sucedería si el puerto configurado en el Healthcheck fuese correcto pero el servidor web dejara de responder?

---

# 🧹 Paso 12. Finalizar la práctica

Detener ambos contenedores.

```bash
docker stop caddy-lab caddy-error
```

Eliminar los contenedores.

```bash
docker rm caddy-lab caddy-error
```

---

## ✅ Verificar la eliminación

Consultar los contenedores existentes.

```bash
docker ps -a
```

Los contenedores **caddy-lab** y **caddy-error** ya no deberán aparecer en la lista.

> 💡 **Buenas prácticas:** Al finalizar un laboratorio elimine los contenedores que ya no se utilizarán. Esto ayuda a mantener un entorno Docker organizado, reduce el consumo de recursos y evita conflictos en futuras prácticas.

> 💡 **Buenas prácticas:** Al finalizar un laboratorio es recomendable eliminar los contenedores que ya no se utilizarán. Esto permite mantener un entorno Docker limpio, evitar el consumo innecesario de recursos y facilitar la ejecución de futuras prácticas.
