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

## Introducción 

En este laboratorio se utilizará la imagen oficial HashiCorp Http-Echo, una aplicación ligera que implementa un servidor HTTP cuyo único propósito es responder con un mensaje configurado por el usuario.

Esta imagen es ampliamente utilizada para pruebas de conectividad, balanceadores de carga, redes Docker y demostraciones básicas de contenedores.

---
## Arquitectura del laboratorio

                         Usuario
                        │
                        │ HTTP
                        ▼
              http://localhost:5678
                        │
                        ▼
        +-------------------------------+
        |  HashiCorp Http-Echo          |
        |                               |
        |  Docker Container             |
        +-------------------------------+
               │      │      │
               │      │      │
               ▼      ▼      ▼
          docker logs
          docker stats
          docker inspect            

---
## Descarga de la imagen

### 1. Consulte las imágenes disponibles

```bash
docker image ls
```
Si la imagen aún no existe, continuar con el siguiente paso.

### 2. Descargar la imagen

```bash
docker pull hashicorp/http-echo
```

### 3. Verificar

```bash
docker image ls
```

  Debe aparecer algo similar a:

```bash
IMAGE                        ID             DISK USAGE   CONTENT SIZE   EXTRA
hashicorp/http-echo:latest   fcb75f691c8b       16.7MB         4.63MB 
```
---

## Crear el contenedor 

```bash
docker run -d \
--name echo-lab \
-p 5678:5678 \
hashicorp/http-echo \
-listen=:5678 \
-text="Bienvenido al laboratorio Docker"
```
Explicación:

| Parámetro             | Descripción                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| `docker run`          | Crea y ejecuta un nuevo contenedor.                                           |
| `-d`                  | Ejecuta el contenedor en segundo plano.                                       |
| `--name echo-lab`     | Asigna el nombre **echo-lab** al contenedor.                                  |
| `-p 5678:5678`        | Publica el puerto 5678 del contenedor en el puerto 5678 del equipo anfitrión. |
| `hashicorp/http-echo` | Imagen utilizada.                                                             |
| `-listen=:5678`       | Configura el servidor HTTP para escuchar en el puerto 5678.                   |
| `-text`               | Define el mensaje que devolverá el servidor.                                  |


---

## Verificar el estado del contenedor

### 1. Consultar los contenedores en ejecución

```bash
docker ps
```
Resultado esperado:

```bash
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                                         NAMES
cdfda4b6005c   hashicorp/http-echo   "/http-echo -listen=…"   48 seconds ago   Up 44 seconds   0.0.0.0:5678->5678/tcp, [::]:5678->5678/tcp   echo-lab
```

--- 

## Probar la aplicación

### Abrir en el navegador web

```bash
http://localhost:5678
```
Debe mostrarse

```bash
Bienvenido al laboratorio Docker
```
### También puede verificarse desde otra terminal mediante:

```bash
curl http://localhost:5678
```
---

## Consultar los registros del contenedor

### Mostrar los registros generados por la aplicación.

```bash
docker logs echo-lab
```

### Monitorear los registros en tiempo real

>- Abrir una segunda terminal

>- Ejecutar:

```bash
docker logs -tf echo-lab
```

>- Actualizar varias veces la página en el navegador.
    Observar cómo aparecen nuevas solicitudes HTTP.
