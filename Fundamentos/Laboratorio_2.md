
# 🐳 Laboratorio 2
# 📊 Monitoreo y Validación Operacional de Contenedores con Grafana

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

En este laboratorio se desplegará una instancia de **Grafana** dentro de un contenedor Docker. Posteriormente se verificará el estado de salud del servicio mediante un **Healthcheck**, se realizarán pruebas de conectividad HTTP y se analizará el comportamiento del contenedor utilizando las principales herramientas de monitoreo y administración proporcionadas por Docker.

Este laboratorio representa un escenario típico utilizado por equipos **DevOps** para validar la disponibilidad de aplicaciones antes de su despliegue en ambientes productivos.

---

# 🏗️ Arquitectura del laboratorio

```text
                           👨‍💻 Cliente
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          │                 Navegador              curl
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │
                         http://localhost:3000
                                │
                                ▼
                 +----------------------------------+
                 |      📊 Grafana Container         |
                 |                                  |
                 |        Docker Engine             |
                 +----------------------------------+
                     │         │           │
                     │         │           │
                     ▼         ▼           ▼
               ❤️ Healthcheck  📊 Stats   🔍 Inspect
                     │
                     ▼
                 📜 Docker Logs
```

> 💡 **Objetivo del laboratorio:** Validar el estado operacional de una aplicación contenerizada mediante pruebas de disponibilidad, monitoreo de recursos y análisis de la configuración interna del contenedor.

---

# 📥 Paso1 1. Descarga de la imagen

En esta primera actividad se descargará la imagen oficial de grafana desde **Docker Hub**. Posteriormente, se verificará que la imagen se encuentre disponible en el repositorio local del equipo

---

# 🚀 Paso 2. Crear el contenedor con Healthcheck

Crear un contenedor denominado **grafana-lab** configurando un **Healthcheck** que verifique periódicamente la disponibilidad del servicio mediante el endpoint `/api/health`.

```bash
docker run -d \
--name grafana-lab \
-p 3000:3000 \
--health-cmd="wget --spider -q http://localhost:3000/api/health || exit 1" \
--health-interval=20s \
--health-timeout=5s \
--health-retries=3 \
--health-start-period=40s \
grafana/grafana
```

### 🔍 Explicación de los parámetros

| Parámetro | Descripción |
|-----------|-------------|
| `docker run` | Crea y ejecuta un nuevo contenedor. |
| `-d` | Ejecuta el contenedor en segundo plano (*Detached Mode*). |
| `--name grafana-lab` | Asigna el nombre **grafana-lab** al contenedor. |
| `-p 3000:3000` | Publica el puerto 3000 del contenedor en el equipo anfitrión. |
| `--health-cmd` | Ejecuta una comprobación HTTP sobre el endpoint `/api/health`. |
| `--health-interval=20s` | Ejecuta el Healthcheck cada 20 segundos. |
| `--health-timeout=5s` | Tiempo máximo permitido para responder al Healthcheck. |
| `--health-retries=3` | Número de fallos consecutivos antes de marcar el contenedor como **unhealthy**. |
| `--health-start-period=40s` | Tiempo de espera antes de iniciar las comprobaciones del Healthcheck. |
| `grafana/grafana` | Imagen oficial de Grafana utilizada para el laboratorio. |

> 💡 **Nota:** El parámetro `--health-start-period` evita que Docker marque el contenedor como **unhealthy** mientras Grafana aún se encuentra inicializando.

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
grafana-lab
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
grafana-lab
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

# 🌐 Paso 5. Acceder a Grafana

Abrir un navegador web y acceder a la siguiente dirección:

```text
http://localhost:3000
```

## 🔐 Credenciales iniciales

| Parámetro | Valor |
|-----------|-------|
| **Usuario** | `admin` |
| **Contraseña** | `admin` |

Durante el primer inicio de sesión, Grafana solicitará el cambio de la contraseña del usuario administrador.

> 💡 **Recomendación:** Utilice una contraseña segura que combine letras mayúsculas, minúsculas, números y caracteres especiales.

---

# 🌍 Paso 6. Verificar la conectividad HTTP

Una vez que Grafana se encuentre en ejecución, verifique la disponibilidad del servicio mediante su endpoint de estado.

Ejecute el siguiente comando desde una nueva terminal:

```bash
curl http://localhost:3000/api/health
```

### 📌 Resultado esperado

```json
{
  "commit":"...",
  "database":"ok",
  "version":"..."
}
```

### 🔍 Interpretación

| Campo | Descripción |
|--------|-------------|
| **commit** | Identificador de la versión compilada de Grafana. |
| **database** | Estado de la base de datos interna. El valor **ok** indica que el servicio funciona correctamente. |
| **version** | Versión instalada de Grafana. |

---

## 📡 Verificar el código de respuesta HTTP

Consultar únicamente las cabeceras HTTP del servicio.

```bash
curl -I http://localhost:3000
```

### 📌 Resultado esperado

```text
HTTP/1.1 302 Found
```

### 🔍 ¿Por qué aparece el código **302 Found**?

Grafana redirige automáticamente las solicitudes realizadas sobre la ruta principal (`/`) hacia la página de autenticación o la interfaz principal del sistema. Esta respuesta confirma que el servidor web está disponible y procesando correctamente las solicitudes HTTP.

> 💡 **Nota:** Un código **302** no representa un error; indica una redirección temporal generada por la propia aplicación.

---

# 📈 Paso 7. Generar tráfico sobre la aplicación

Con el objetivo de observar el comportamiento del contenedor bajo carga, genere actividad sobre la interfaz web de Grafana.

Realice las siguientes acciones desde el navegador:

- 🔑 Iniciar sesión.
- 🔄 Actualizar repetidamente el Dashboard.
- ⚙️ Acceder al menú **Administration**.
- 🛠️ Acceder al menú **Configuration**.
- 🏠 Regresar a la página principal.

Mientras realiza estas acciones, abra otra terminal y ejecute:

```bash
docker stats
```

## 📊 Analizar las siguientes métricas

| Métrica | Descripción |
|----------|-------------|
| ⚙️ **CPU %** | Porcentaje de utilización del procesador. |
| 🧠 **MEM USAGE** | Memoria consumida por el contenedor. |
| 🌐 **NET I/O** | Tráfico de red recibido y transmitido. |

> 💡 **Pregunta de análisis:** ¿Cuál de las tres métricas presentó la mayor variación durante la interacción con Grafana?

---

# 🔍 Paso 8. Inspeccionar el contenedor

Consultar la configuración completa del contenedor.

```bash
docker inspect grafana-lab
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
grafana-lab
```

### 💡 Pregunta de análisis

¿Por qué Docker asigna una dirección IP privada al contenedor si el servicio ya se encuentra publicado mediante el puerto **3000**?

---

# 🖥️ Paso 9. Analizar los procesos del contenedor

Consultar los procesos que actualmente se encuentran ejecutándose dentro del contenedor.

```bash
docker top grafana-lab
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
docker logs -tf grafana-lab
```

## 🔍 Opciones utilizadas

| Opción | Descripción |
|---------|-------------|
| `-t` | Muestra la fecha y hora de cada evento registrado. |
| `-f` | Mantiene la visualización de los registros en tiempo real (*Follow Mode*). |

---

## 📈 Generar actividad sobre Grafana

Mientras el comando permanece ejecutándose, realice las siguientes acciones desde el navegador:

- 🔄 Actualice varias veces la página principal.
- 🔑 Inicie sesión en Grafana.
- ⚙️ Acceda a los menús **Administration** y **Configuration**.
- 🏠 Regrese al Dashboard principal.

Observe cómo aparecen nuevos eventos en la terminal cada vez que Grafana recibe una solicitud HTTP.

> 💡 **Nota:** Para finalizar la visualización de los registros utilice la combinación de teclas **Ctrl + C**.

---

# ❤️ Paso 11. Simular un fallo del Healthcheck

En esta actividad se desplegará un segundo contenedor con un **Healthcheck** configurado de forma incorrecta. El objetivo es comparar el comportamiento de un servicio **healthy** con otro **unhealthy**.

Crear el segundo contenedor.

```bash
docker run -d \
--name grafana-error \
-p 3001:3000 \
--health-cmd="wget --spider -q http://localhost:3000/noexiste || exit 1" \
--health-interval=10s \
--health-retries=2 \
grafana/grafana
```

Espere aproximadamente **60 segundos** para que Docker ejecute varias comprobaciones del Healthcheck.

---

## 📊 Comparar el estado de ambos contenedores

Consultar los contenedores en ejecución.

```bash
docker ps
```

### 📌 Resultado esperado

| Contenedor | Estado esperado |
|-------------|----------------|
| 🟢 **grafana-lab** | `Up (healthy)` |
| 🔴 **grafana-error** | `Up (unhealthy)` |

Observe que ambos contenedores continúan ejecutándose, pero únicamente uno de ellos responde correctamente al Healthcheck.

---

## 🔍 Verificar el estado del Healthcheck

Consultar únicamente el estado del contenedor con error.

```bash
docker inspect \
--format='{{.State.Health.Status}}' \
grafana-error
```

### 📌 Resultado esperado

```text
unhealthy
```

---

## 💡 Preguntas de análisis

1. ¿Por qué el contenedor **grafana-error** permanece en ejecución aunque su estado sea **unhealthy**?
2. ¿Cuál es la diferencia entre el estado **Up** mostrado por `docker ps` y el estado reportado por el **Healthcheck**?
3. ¿Qué utilidad tendría esta información en plataformas como Docker Compose, Docker Swarm o Kubernetes?

---

# 🧹 Paso 12. Finalizar la práctica

Una vez concluidas las pruebas, detenga ambos contenedores.

```bash
docker stop grafana-lab grafana-error
```

Eliminar los contenedores.

```bash
docker rm grafana-lab grafana-error
```

---

## ✅ Verificar la eliminación

Consultar los contenedores existentes.

```bash
docker ps -a
```

Los contenedores **grafana-lab** y **grafana-error** ya no deberán aparecer en la lista.

> 💡 **Buenas prácticas:** Al finalizar un laboratorio es recomendable eliminar los contenedores que ya no se utilizarán. Esto permite mantener un entorno Docker limpio, evitar el consumo innecesario de recursos y facilitar la ejecución de futuras prácticas.
