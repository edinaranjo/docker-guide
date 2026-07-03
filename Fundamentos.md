
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

# 🔍 Paso 2. Verificar la instalación

Comprobar la versión instalada.

```bash
docker --version
```

Salida esperada:

```text
Docker version XX.X.X
```

---

# ⚙️ Paso 3. Administrar el servicio Docker

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
