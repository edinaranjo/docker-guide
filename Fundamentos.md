
# 🚀 Instalación de Docker Engine

Ejecute el siguiente comando:

```bash
sudo apt install docker* -y
```

> **¿Qué realiza este comando?**
>
> - Descarga Docker desde los repositorios de Debian/Ubuntu.
> - Instala Docker Engine.
> - Instala Docker CLI.
> - Instala el servicio `dockerd`.
> - Configura las dependencias necesarias.

Nota: Esta instalación es para distribuciones basadas en Debian

---

# 🔍 Verificación de la instalación

Comprobar la versión instalada.

```bash
docker --version
```

Salida esperada:

```text
Docker version XX.X.X
```

---

# ⚙️ Administración del servicio Docker

Docker funciona como un servicio del sistema operativo.

## ▶️ Iniciar el servicio

```bash
sudo systemctl start docker
```

Este comando inicia Docker inmediatamente.

---

## 🔄 Configurar el inicio automático

```bash
sudo systemctl enable docker
```

A partir del siguiente reinicio del sistema operativo, Docker iniciará automáticamente.

---

## 📊 Verificar el estado

```bash
sudo systemctl status docker
```

Salida esperada:

```text
Active: active (running)
```

---

## ⏹️ Detener el servicio

```bash
sudo systemctl stop docker
```

Utilice este comando cuando desee detener completamente Docker.

---

## 🔁 Reiniciar el servicio

```bash
sudo systemctl restart docker
```

Este comando es útil cuando se realizan cambios en la configuración del servicio.

---

# 📌 Resumen de comandos

| Comando | Acción |
|----------|--------|
| `systemctl start docker` | Inicia el servicio |
| `systemctl stop docker` | Detiene el servicio |
| `systemctl restart docker` | Reinicia el servicio |
| `systemctl status docker` | Muestra el estado actual |
| `systemctl enable docker` | Habilita el inicio automático |

---

# 🐋 Paso 4. Ejecutar el primer contenedor

Docker proporciona una imagen denominada **hello-world**, diseñada para comprobar que la instalación funciona correctamente.

Ejecute:

```bash
docker run hello-world
```

Si la instalación fue correcta observará un mensaje similar al siguiente:

```text
Hello from Docker!

This message shows that your installation appears to be working correctly.
```

---

# 🔎 ¿Qué ocurrió internamente?

Cuando ejecutó el comando anterior, Docker realizó automáticamente las siguientes acciones:

```text
Docker Client
        │
        ▼
Docker Daemon
        │
        ▼
Buscar imagen hello-world
        │
        ▼
Docker Hub
        │
        ▼
Descargar imagen
        │
        ▼
Crear contenedor
        │
        ▼
Ejecutar aplicación
```

Todo este proceso ocurre automáticamente mediante un único comando.

---

# 📦 Paso 5. Verificar las imágenes descargadas

```bash
docker images
```

Ejemplo:

```text
REPOSITORY     TAG       IMAGE ID        SIZE
hello-world    latest    xxxxxxxxxxxx    13.3kB
```

Observe que ahora existe una imagen almacenada localmente.

---

# 📦 Paso 6. Verificar los contenedores

Mostrar únicamente los contenedores en ejecución.

```bash
docker ps
```

No aparecerá ningún contenedor, ya que **hello-world** finaliza inmediatamente después de mostrar el mensaje.

---

Mostrar todos los contenedores.

```bash
docker ps -a
```

Salida esperada:

```text
CONTAINER ID
IMAGE
STATUS
```

Observe que el contenedor permanece registrado, aunque ya terminó su ejecución.

---

# 🧹 Paso 7. Eliminar el contenedor

Eliminar el contenedor utilizando su ID o nombre.

```bash
docker rm <ID_CONTENEDOR>
```

Verificar nuevamente.

```bash
docker ps -a
```

---

# 🗑️ Paso 8. Eliminar la imagen

```bash
docker rmi hello-world
```

Comprobar que ya no existen imágenes.

```bash
docker images
```

---

---
