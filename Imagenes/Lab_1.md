# ⚡ Guía rápida: Crear una imagen personalizada con NGINX

> **Objetivo:** construir una imagen Docker personalizada usando un `Dockerfile` y una página `index.html`, para desplegar un servidor web NGINX en un contenedor.

---

## 📁 Estructura del laboratorio

Cree una carpeta de trabajo:

```bash
mkdir nginx-lab
cd nginx-lab
```

La estructura final debe quedar así:

```text
nginx-lab/
├── Dockerfile
└── index.html
```

El archivo `index.html` corresponde a la página personalizada adjunta, que muestra el mensaje **“¡NGINX en marcha!”** y confirma el despliegue del servidor web con Docker. :contentReference[oaicite:0]{index=0}

---

## 🐳 Paso 1. Crear el Dockerfile

Dentro de la carpeta `nginx-lab`, cree el archivo:

```bash
nano Dockerfile
```

Agregue el siguiente contenido:

```dockerfile
FROM nginx:latest

COPY index.html /usr/share/nginx/html/index.html
```

### 🔎 Explicación rápida

| Instrucción | Descripción |
|------------|-------------|
| `FROM nginx:latest` | Usa la imagen oficial de NGINX como base. |
| `COPY index.html ...` | Copia la página personalizada al directorio web de NGINX. |

---

## 🏗️ Paso 2. Construir la imagen

Ejecute:

```bash
docker build -t nginx-personalizado:v1 .
```

### ¿Qué hace este comando?

| Elemento | Significado |
|---------|-------------|
| `docker build` | Construye una imagen a partir del Dockerfile. |
| `-t nginx-personalizado:v1` | Asigna nombre y versión a la imagen. |
| `.` | Usa la carpeta actual como contexto de construcción. |

---

## 📦 Paso 3. Verificar la imagen creada

```bash
docker image ls
```

Debe aparecer una imagen similar a:

```text
REPOSITORY             TAG       IMAGE ID       CREATED          SIZE
nginx-personalizado    v1        xxxxxxxxxxxx   Few seconds ago  xxxMB
```

---

## 🚀 Paso 4. Crear y ejecutar el contenedor

```bash
docker run -d \
  --name web-nginx-lab \
  -p 8080:80 \
  nginx-personalizado:v1
```

### 🔎 Explicación

| Parámetro | Descripción |
|----------|-------------|
| `-d` | Ejecuta el contenedor en segundo plano. |
| `--name web-nginx-lab` | Asigna un nombre al contenedor. |
| `-p 8080:80` | Publica el puerto 80 del contenedor en el puerto 8080 del host. |
| `nginx-personalizado:v1` | Imagen personalizada utilizada. |

---

## 🌐 Paso 5. Probar el servicio web

Abra en el navegador:

```text
http://localhost:8080
```

También puede probar desde la terminal:

```bash
curl http://localhost:8080
```

Debe visualizarse la página personalizada de NGINX.

---

## 🔍 Paso 6. Verificar el contenedor

```bash
docker ps
```

Resultado esperado:

```text
CONTAINER ID   IMAGE                    STATUS       PORTS                  NAMES
xxxxxxxxxxxx   nginx-personalizado:v1    Up ...       0.0.0.0:8080->80/tcp   web-nginx-lab
```

---

## 📄 Paso 7. Consultar logs

```bash
docker logs web-nginx-lab
```

Para monitorear en tiempo real:

```bash
docker logs -f web-nginx-lab
```

---

## 🧹 Paso 8. Limpieza del laboratorio

Detener el contenedor:

```bash
docker stop web-nginx-lab
```

Eliminar el contenedor:

```bash
docker rm web-nginx-lab
```

Eliminar la imagen:

```bash
docker rmi nginx-personalizado:v1
```

---

## ✅ Resumen de comandos

| Acción | Comando |
|-------|---------|
| Construir imagen | `docker build -t nginx-personalizado:v1 .` |
| Listar imágenes | `docker image ls` |
| Ejecutar contenedor | `docker run -d --name web-nginx-lab -p 8080:80 nginx-personalizado:v1` |
| Ver contenedores | `docker ps` |
| Ver logs | `docker logs web-nginx-lab` |
| Detener contenedor | `docker stop web-nginx-lab` |
| Eliminar contenedor | `docker rm web-nginx-lab` |
| Eliminar imagen | `docker rmi nginx-personalizado:v1` |

---

## 🎯 Competencia DevOps

Con esta práctica se construye una imagen personalizada, se despliega un contenedor web y se valida su funcionamiento, reproduciendo un flujo básico de construcción y despliegue usado en entornos DevOps.
