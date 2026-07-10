# 🚀 Trabajo Final 

![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitFlow](https://img.shields.io/badge/GitFlow-Workflow-blue?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)
![DevOps](https://img.shields.io/badge/DevOps-Final%20Project-blueviolet?style=for-the-badge)

---

## 📁 Paso 1. Crear el directorio del proyecto llamado proyecto-final-devops 

---

## 🌿 Paso 2. Inicializar Git y Git Flow dentro del directorio del proyecto

---

## 📁 Paso 3. Crear la estructura del proyecto

```text
📁 proyecto-final-devops
│
├── 📁 app
│   ├── 📄 main.py
│   │
│   └── 📁 templates
│       └── 📄 index.html
│
├── 📄 requirements.txt
│
├── 📄 Dockerfile
│
└── 📄 .dockerignore
```
---

##  📄 Paso 4. Agregar el contenido

Copie en cada archivo el contenido proporcionado en este repositorio.

Los archivos son:

| Archivo | Descripción |
|----------|-------------|
| `main.py` | Aplicación principal |
| `index.html` | Página web |
| `requirements.txt` | Dependencias Python |
| `Dockerfile` | Construcción de la imagen Docker |
| `.dockerignore` | Exclusión de archivos durante la construcción |

---

# 💾 Paso 5. Confirmar los cambios

Realice las operaciones necesarias de git y gitflow para agregar y confirmar sus archivos en el repositorio. Utilice commits adecuados.

---

# 🚀 Paso 6. Crear la versión Release

Cree el versionamiento de la aplicación usando una rama release

--- 

# 📤 Paso 7. Envie el contenido del directorio y las etiquetas a un repositorio en GitHub que tenga el mismo nombre.

---

# ⚙️ Paso 8. Crear el workflow de GitHub Actions

Elabore un workflow en GitHub Actions para crear la imagen usando el Dockerfile y subirla a DockerHub. El nombre de la imagen será devops-final-project:v1. Adjunte el código del workflow y una captura de pantalla de la imagen subida en Docker Hub en su repositorio.

--- 

# 🐳 Paso 9. Crear el contenedor

Cada grupo deberá ejecutar la imagen publicada en Docker Hub utilizando variables de entorno.

## Sintaxis general

```bash
docker run -d \
  --name devops-final-project \
  -p <PUERTO_HOST>:8000 \
  -e GROUP_NAME="<Número del grupo>" \
  -e GROUP_MEMBERS="<Integrante1, Integrante2>" \
  -e COURSE_NAME="<Nombre del curso>" \
  <usuario>/devops-final-project:v1
```

---

## Ejemplo para el Grupo 1

```bash
docker run -d \
  --name devops-final-project \
  -p 8000:8000 \
  -e GROUP_NAME="Grupo 1" \
  -e GROUP_MEMBERS="Ana, Luis, Carlos" \
  -e COURSE_NAME="Curso de Profesionalización en DevOps" \
  edinaranjoespin/devops-final-project:v1
```

---

## 🔍 Descripción del comando

| Parámetro | Función |
|---|---|
| `-d` | Ejecuta el contenedor en segundo plano. |
| `--name` | Asigna un nombre al contenedor. |
| `-p` | Publica el puerto de la aplicación. |
| `-e` | Define una variable de entorno. |
| `GROUP_NAME` | Identifica al grupo. |
| `GROUP_MEMBERS` | Registra los nombres de los integrantes. |
| `COURSE_NAME` | Muestra el nombre del curso. |
| `:v1` | Selecciona la versión de la imagen. |

---

# 🔌 Asignación de puertos por grupo

Cada grupo deberá utilizar un puerto diferente en el equipo host.

| Grupo | Puerto host | URL |
|---:|---:|---|
| Grupo 1 | `8001` | `http://localhost:8001` |
| Grupo 2 | `8002` | `http://localhost:8002` |
| Grupo 3 | `8003` | `http://localhost:8003` |
| Grupo 4 | `8004` | `http://localhost:8004` |
| Grupo 5 | `8005` | `http://localhost:8005` |

El puerto interno de la aplicación permanece en `8000`.

Por ejemplo, para el Grupo 3:

```bash
docker run -d \
  --name devops-final-project-grupo3 \
  -p 8003:8000 \
  -e GROUP_NAME="Grupo 3" \
  -e GROUP_MEMBERS="Integrante 1, Integrante 2" \
  -e COURSE_NAME="Curso de Profesionalización en DevOps" \
  <usuario>/devops-final-project:v1
```

> 💡 Si varios grupos ejecutan los contenedores en equipos diferentes, podrían reutilizar el mismo puerto. Sin embargo, para esta actividad se solicita usar puertos distintos con fines de identificación.

---

# 📦 Paso 10. Verificar la imagen

Ejecutar:

```bash
docker image ls
```

También puede aplicar un filtro:

```bash
docker image ls | grep devops-final-project
```

Resultado de referencia:

```text
REPOSITORY                               TAG   IMAGE ID       CREATED          SIZE

<usuario>/devops-final-project           v1    f8ca9ff47071   2 minutes ago    232MB
```

> 📌 Los valores de `IMAGE ID`, fecha y tamaño pueden variar entre equipos.

---

# 🖥️ Paso 11. Verificar el contenedor

Ejecutar:

```bash
docker ps -a
```

También puede filtrar el resultado:

```bash
docker ps -a --filter "name=devops-final-project"
```

Resultado de referencia:

```text
CONTAINER ID   IMAGE                                  COMMAND                  STATUS                    PORTS                    NAMES

1f96176d6b57   usuario/devops-final-project:v1        "sh -c 'uvicorn...'"    Up 2 minutes (healthy)    0.0.0.0:8001->8000/tcp   devops-final-project
```

---

### ❤️ Estado esperado

El contenedor debe mostrar:

```text
Up (...) (healthy)
```

Esto confirma que:

- El proceso de FastAPI está activo.
- Uvicorn responde en el puerto configurado.
- El endpoint `/health` funciona.
- El healthcheck definido en el Dockerfile fue superado.

---

### 🔍 Verificar únicamente el estado de salud

```bash
docker inspect \
  --format='{{.State.Health.Status}}' \
  devops-final-project
```

Resultado esperado:

```text
healthy
```

---

# 🌐 Paso 12. Probar la aplicación

Abrir en el navegador:

```text
http://localhost:<puerto>
```

Ejemplo para el Grupo 1:

```text
http://localhost:8001
```

Ejemplo para el Grupo 3:

```text
http://localhost:8003
```

La página debe mostrar:

- Número o nombre del grupo.
- Nombres de los integrantes.
- Nombre del curso.
- Estado del servicio.
- Entorno de ejecución.
- Información del contenedor.
- Endpoints disponibles.

---

## 🧪 Probar endpoints adicionales

### Healthcheck

```bash
curl http://localhost:8001/health
```

### Información de la aplicación

```bash
curl http://localhost:8001/info
```

### Métricas básicas

```bash
curl http://localhost:8001/metrics
```

Cambie `8001` por el puerto asignado a su grupo.

---

## 📸 Evidencia requerida de la página de inicio

Tome una captura de pantalla donde se observe:

- La URL utilizada.
- La página completa.
- El nombre del grupo.
- Los integrantes.
- El nombre del curso.

Adjunte una captura de pantalla de la pagina de incio del contenedor.

---

# 📝 Paso 14. Elaborar el informe técnico

El informe debe crearse en formato Markdown y permanecer en la raíz del proyecto.

Nombre recomendado:

```text
INFORME.md
```

La raíz deberá contener:

```text
📁 proyecto-final-devops
├── 📄 README.md
├── 📄 INFORME.md
├── 📄 Dockerfile
├── 📄 requirements.txt
├── 📄 .dockerignore
└── ...
```

---

## 📑 Estructura mínima del informe

```markdown
# Informe del Trabajo Final DevOps

## 1. Datos del grupo

## 2. Objetivos

## 3. Estructura del proyecto

## 4. Configuración de Git y GitFlow

## 5. Historial de commits

## 6. Creación de la release

## 7. Publicación en GitHub

## 8. Configuración de GitHub Actions

## 9. Publicación en Docker Hub

## 10. Ejecución del contenedor

## 11. Verificación de la imagen

## 12. Verificación del contenedor

## 13. Pruebas de funcionamiento

## 14. Resultados

## 15. Conclusiones
```
