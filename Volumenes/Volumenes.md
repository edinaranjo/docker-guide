Aquí tienes una propuesta de archivo **README.md** profesional y didáctico sobre los **Volúmenes en Docker**, diseñado para GitHub y basado íntegramente en la información técnica de tus fuentes.

---

# 💾 Guía Profesional: Volúmenes y Persistencia en Docker

En el ecosistema de contenedores, la **persistencia de datos** es un pilar fundamental. Por defecto, cualquier archivo creado dentro de un contenedor se pierde permanentemente al eliminarlo. Esta guía detalla cómo Docker soluciona este problema mediante el manejo eficiente de datos.

---

## 🧐 1. ¿Por qué necesitamos Volúmenes?

Imagina desplegar una base de datos **MySQL**; sin un mecanismo de persistencia, toda tu información desaparecería al detener o borrar el contenedor. Para evitar esto, Docker ofrece diversas estrategias de almacenamiento:

*   **📦 Volúmenes:** Son gestionados directamente por Docker en una parte específica del sistema de archivos del host (`/var/lib/docker/volumes/`). Es la opción recomendada para **producción**.
*   **🔗 Bind Mounts:** Enlazan una carpeta específica del host con el contenedor. Son ideales para el **desarrollo**, ya que permiten el *hot-reload* (los cambios en el código del host se reflejan al instante).
*   **⚡ tmpfs:** Se monta en la memoria RAM del sistema. Útil para datos temporales o sensibles que no deben persistir en el disco.

---

## 🛠️ 2. Comandos de Administración

La gestión profesional de volúmenes se realiza a través de los siguientes comandos:

| Acción | Comando | Descripción |
| :--- | :--- | :--- |
| **Crear** | `docker volume create <nombre>` | Inicializa un nuevo volumen gestionado. |
| **Listar** | `docker volume ls` | Muestra todos los volúmenes existentes. |
| **Inspeccionar** | `docker volume inspect <nombre>` | Muestra detalles técnicos y la ruta en el host. |
| **Eliminar** | `docker volume rm <nombre>` | Borra un volumen específico (no debe estar en uso). |

---

## 🚀 3. Implementación Práctica

### 🌐 Uso de Volúmenes (Producción)
Para ejecutar un servidor Nginx cuya web persista aunque el contenedor se borre:
```bash
docker run -d \
  --name nginx_persitente \
  -v mi_volumen:/usr/share/nginx/html \
  -p 8080:80 \
  nginx
```

### 🗄️ Persistencia en Bases de Datos
*   **MySQL con Volúmenes:** `docker run -d -v mysql_datos:/var/lib/mysql mysql:8`.
*   **PostgreSQL con Bind Mount:** `docker run -d -v ~/postgres_data:/var/lib/postgresql/data postgres:15`.

---

## 🔄 4. Estrategias Avanzadas: Backup y Restore

Docker permite realizar copias de seguridad de volúmenes críticos utilizando contenedores temporales (como `busybox`):

1.  **Backup:** Empaqueta el contenido del volumen en un archivo `.tar` en tu host.
2.  **Restore:** Extrae un archivo `.tar` de respaldo directamente dentro de un volumen nuevo o vacío.

---

## ✅ 5. Buenas Prácticas Profesionales

Para un despliegue de nivel empresarial, sigue estos lineamientos:
*   **Prioriza Volúmenes en Producción:** Son más seguros, portables y gestionables que los bind mounts.
*   **Nombres Descriptivos:** Utiliza nombres claros como `db_data_prod` o `uploads_v1`.
*   **Backups Regulares:** Realiza respaldos constantes de los volúmenes que contienen bases de datos críticas.
*   **Seguridad:** Evita exponer datos sensibles mediante bind mounts con permisos incorrectos en el host.

---
*Este material forma parte de la Unidad 2: Imágenes, volúmenes y redes en Docker.*
