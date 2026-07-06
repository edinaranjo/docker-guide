

# 🐳 Imágenes en Docker

Bienvenido a esta guía esencial sobre el manejo de **imágenes en Docker**. Las imágenes son el componente fundamental para el despliegue moderno de aplicaciones, actuando como la base de la portabilidad y eficiencia en la industria.

---

## 🖼️ 1. ¿Qué es una Imagen en Docker?

Una imagen de Docker es una **plantilla inmutable** que sirve como modelo para crear contenedores. Contiene todo lo necesario para que una aplicación funcione:
*   📦 **Sistema de archivos:** Dependencias, librerías y configuraciones.
*   📜 **Instrucciones:** Pasos específicos para ejecutar la aplicación.

> [!TIP]
> **Analogía Didáctica:** Piensa en la **imagen** como una 📜 *receta* y en el **contenedor** como el 🍽️ *plato ya preparado*.

### ✨ Características Principales
*   **Capas (layers):** Cada instrucción genera una capa, permitiendo que sean reutilizables y ligeras.
*   **Inmutabilidad:** Una vez creada, la imagen no cambia.
*   **Portabilidad:** Se comparten fácilmente en registros como **Docker Hub**.
*   **Eficiencia:** Varias imágenes pueden compartir capas, optimizando el espacio en disco.

---

## 🛠️ 2. Administración de Imágenes

Para gestionar imágenes de manera profesional, utilizamos los siguientes comandos esenciales:

| Acción | Comando | Descripción |
| :--- | :--- | :--- |
| **Extraer** | `docker pull <image-name>` | Descarga una imagen desde un repositorio. |
| **Listar** | `docker images` | Muestra todas las imágenes disponibles localmente. |
| **Eliminar** | `docker image rm <id>` | Borra una imagen específica (si no está en uso). |
| **Limpiar** | `docker image prune -a` | Elimina todas las imágenes que no están siendo usadas por contenedores. |

---

## 🏗️ 3. Creación de Imágenes: El Dockerfile

Un **Dockerfile** es un archivo de texto plano que contiene las instrucciones para ensamblar una imagen.

### 📑 Instrucciones Clave
*   `FROM`: Define la imagen base (obligatorio).
*   `WORKDIR`: Establece el directorio de trabajo dentro del contenedor.
*   `RUN`: Ejecuta comandos (como instalar paquetes) y crea una nueva capa.
*   `COPY` / `ADD`: Copian archivos del host al contenedor.
*   `ENV` / `ARG`: Definen variables de entorno o de construcción.
*   `EXPOSE`: Informa sobre los puertos en los que escucha el contenedor.
*   `CMD`: Define el comando por defecto al iniciar el contenedor.

---





## 🚀 4. Optimización con Multi-stage Builds

Para despliegues profesionales, se recomienda el uso de **imágenes multi-stage**. Esto permite usar varias etapas (`FROM`) en un solo Dockerfile.

### ⚖️ Comparativa de Eficiencia
| Característica | Single-stage | Multi-stage |
| :--- | :--- | :--- |
| **Tamaño Final** | Pesado (incluye compiladores) | **Muy Ligero** (solo el binario) |
| **Seguridad** | Menor (mayor superficie de ataque) | **Alta** (sin herramientas innecesarias) |
| **Velocidad** | Lenta de mover/desplegar | **Rápida** de desplegar |

**Ejemplo de impacto en el peso:**
*   Imagen Single-stage (C): **200 MB**.
*   Imagen Multi-stage (C): **5 MB**.

---

## 🧪 5. Prácticas de Aprendizaje

Para dominar este contenido, el documento sugiere las siguientes prácticas:
1.  **Nginx Personalizado:** Crear y desplegar una imagen de servidor web.
2.  **App Python/FastAPI:** Empaquetar aplicaciones modernas.
3.  **Compilación en C:** Comparar la diferencia de peso entre single-stage y multi-stage.

---
*Guía generada con fines educativos basada en la Unidad 2 de Capacitación en Docker.*

