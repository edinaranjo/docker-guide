# 🐳 Laboratorio: Despliegue Automatizado con Docker Compose y Healthcheck

![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-000000?style=for-the-badge&logo=flask&logoColor=white)
![DevOps](https://img.shields.io/badge/DevOps-Laboratory-blueviolet?style=for-the-badge)

---

## 🎯 Objetivos

Al finalizar este laboratorio el estudiante será capaz de:

- 🐳 Construir una imagen Docker personalizada mediante un **Dockerfile**.
- ⚙️ Automatizar el despliegue de una aplicación utilizando **Docker Compose**.
- ❤️ Implementar un **Healthcheck** para verificar automáticamente la disponibilidad del servicio.
- 📊 Supervisar el estado de los contenedores mediante Docker.
- 📜 Analizar los registros generados por la aplicación durante su ejecución.

---

# 📖 Escenario

Una empresa desea desplegar una aplicación web interna para verificar el estado operativo de sus servicios.

Para automatizar el despliegue se utilizarán las siguientes tecnologías:

- 🐍 Flask
- 🐳 Docker
- ⚙️ Docker Compose
- ❤️ Docker Healthcheck

La aplicación expondrá dos rutas:

| Ruta | Función |
|-------|----------|
| `/` | Página principal |
| `/health` | Estado del servicio |

---

# 📁 Estructura del proyecto

```text
app-healthcheck/
│
├── app/
│   ├── main.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
├── Dockerfile
│
└── docker-compose.yml
```

---

# 🚀 Paso 1. Crear la aplicación Flask

Archivo:

```text
app/main.py
```

```python
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "app-devops",
        "message": "El servicio responde correctamente"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

> 💡 La ruta `/health` será utilizada por Docker para comprobar automáticamente la salud del contenedor.

---

# 🎨 Paso 2. Crear la interfaz web

Archivo:

```text
app/templates/index.html
```

La página mostrará:

- 🐳 Nombre del laboratorio
- ❤️ Estado del servicio
- 📦 Información del despliegue
- ⚙️ Docker Compose
- 📊 Logs
- ❤️ Healthcheck

El contenido completo del archivo se encuentra en este repositorio.

---

# 🎨 Paso 3. Crear la hoja de estilos

Archivo

```text
app/static/style.css
```

La hoja de estilos proporciona:

- 🎨 Diseño moderno
- 📱 Diseño adaptable (Responsive)
- 🌙 Tema oscuro
- 📦 Tarjetas informativas
- 🟢 Indicadores visuales del estado del servicio

---

# 🏗️ Paso 4. Crear el Dockerfile

Archivo

```text
Dockerfile
```

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY app/ .

RUN pip install flask

EXPOSE 5000

CMD ["python","main.py"]
```

## 🔍 Explicación

| Instrucción | Función |
|-------------|----------|
| FROM | Imagen base |
| WORKDIR | Directorio de trabajo |
| COPY | Copia la aplicación |
| RUN | Instala Flask |
| EXPOSE | Publica el puerto |
| CMD | Ejecuta la aplicación |

---

# ⚙️ Paso 5. Crear Docker Compose

Archivo

```text
docker-compose.yml
```

```yaml
services:

  web:

    build: .

    container_name: app-devops

    ports:
      - "5000:5000"

    restart: always

    healthcheck:
      test:
        [
          "CMD",
          "python",
          "-c",
          "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"
        ]

      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 10s
```

---

# ❤️ ¿Qué hace el Healthcheck?

Docker ejecutará periódicamente la siguiente comprobación:

```text
http://localhost:5000/health
```

Si la respuesta es satisfactoria:

```text
healthy
```

Si la aplicación deja de responder:

```text
unhealthy
```

---

# 🚀 Paso 6. Construir y desplegar

Desde la carpeta del proyecto ejecutar:

```bash
docker compose up -d
```

Este único comando realiza automáticamente:

- 📦 Construcción de la imagen
- 🌐 Creación de la red
- ▶️ Inicio del contenedor
- ❤️ Configuración del Healthcheck

---

# 🔍 Paso 7. Verificar el despliegue

Consultar los contenedores:

```bash
docker compose ps
```

Resultado esperado:

```text
NAME         STATUS

app-devops   Up (healthy)
```

---

# 🌐 Paso 8. Acceder a la aplicación

Abrir en el navegador:

```text
http://localhost:5000
```

Se mostrará una interfaz similar a:

```
🐳 DevOps Docker Compose Lab

✔ Aplicación funcionando correctamente

Dockerfile

Docker Compose

Healthcheck

Logs
```

---

# ❤️ Paso 9. Verificar la salud

Abrir:

```text
http://localhost:5000/health
```

Respuesta:

```json
{
    "status":"healthy",
    "service":"app-devops",
    "message":"El servicio responde correctamente"
}
```

---

# 📜 Paso 10. Visualizar los logs

Ver todos los registros:

```bash
docker compose logs
```

Seguir los registros en tiempo real:

```bash
docker compose logs -f
```

---

# 📊 Paso 11. Inspeccionar el Healthcheck

Consultar el estado del contenedor:

```bash
docker inspect app-devops
```

Consultar únicamente la información del Healthcheck:

```bash
docker inspect --format='{{json .State.Health}}' app-devops
```

---

# ⚠️ Paso 12. Simular un fallo

Ingresar al contenedor:

```bash
docker exec -it app-devops sh
```

Detener la aplicación:

```bash
pkill -f main.py
```

Salir del contenedor:

```bash
exit
```

Comprobar nuevamente:

```bash
docker compose ps
```

Después de algunos segundos el estado cambiará a:

```text
unhealthy
```

---

# 🔄 Paso 13. Recuperar el servicio

Reiniciar el contenedor:

```bash
docker compose restart
```

Verificar:

```bash
docker compose ps
```

Resultado esperado:

```text
Up (healthy)
```

---

# 🧹 Paso 14. Finalizar el laboratorio

Detener el entorno:

```bash
docker compose down
```

---

# 🧠 Actividades propuestas

Realice las siguientes actividades:

- ✅ Modifique el mensaje mostrado en la página principal.
- ✅ Cambie el color principal de la interfaz.
- ✅ Agregue un nuevo apartado denominado **Información del Contenedor**.
- ✅ Agregue un nuevo campo al JSON de `/health`.
- ✅ Cambie el intervalo del Healthcheck de **10 segundos** a **30 segundos**.
- ✅ Observe el comportamiento del contenedor cuando la aplicación deja de responder.

---

# 💡 Preguntas de reflexión

1. ¿Qué ventajas ofrece Docker Compose frente al uso de múltiples comandos `docker run`?

2. ¿Cuál es la función del archivo `Dockerfile`?

3. ¿Por qué es importante implementar un Healthcheck?

4. ¿Qué diferencia existe entre un contenedor **Up** y uno **Up (healthy)**?

5. ¿Qué utilidad tienen los logs durante la operación de una aplicación?

6. ¿Cómo podría integrarse este laboratorio dentro de un Pipeline DevOps?

---

# 🎯 Conclusiones

En este laboratorio se aplicaron conceptos fundamentales de **Docker** y **Docker Compose** para automatizar el despliegue de una aplicación web basada en Flask.

Además, se implementó un **Healthcheck** que permite verificar automáticamente la disponibilidad del servicio y se utilizaron las herramientas de monitoreo de Docker para analizar el comportamiento del contenedor durante su ejecución.

Este flujo representa una práctica habitual en proyectos DevOps y constituye la base para integrar posteriormente procesos de **Integración Continua (CI)** y **Despliegue Continuo (CD)** mediante plataformas como GitLab CI/CD, GitHub Actions o Jenkins.

---

## 📚 Recursos recomendados

- 📖 https://docs.docker.com/
- 📖 https://docs.docker.com/compose/
- 📖 https://flask.palletsprojects.com/
- 📖 https://hub.docker.com/

---

<div align="center">

### 🚀 Curso de Profesionalización en DevOps

**Docker • Docker Compose • Automatización • Healthcheck • Monitoreo**

</div>
