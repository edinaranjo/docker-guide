# 🐳 Laboratorio: Administración y Monitoreo de Contenedores con HashiCorp Http-Echo

## Objetivos

Al finalizar esta práctica el estudiante será capaz de:

>- Desplegar una aplicación HTTP utilizando Docker.
>- Comprender el ciclo de vida de un contenedor.
>- Acceder al contenedor mediante docker exec.
>- Analizar el consumo de recursos con docker stats.
>- Consultar los registros generados mediante docker logs.
>- Visualizar los procesos internos utilizando docker top.
>- Inspeccionar la configuración del contenedor.
>- Implementar y verificar un Healthcheck.

---

## Escenario

En este laboratorio se desplegará un pequeño servidor HTTP basado en la imagen oficial HashiCorp Http-Echo, el cual responderá siempre con un mensaje personalizado.

Posteriormente se realizarán diferentes tareas administrativas para analizar el comportamiento del contenedor.

---
## Arquitectura del laboratorio

                    Navegador Web
                           │
                    http://localhost:5678
                           │
                           ▼
              +-----------------------------+
              |  HashiCorp Http-Echo        |
              |     Docker Container        |
              +-----------------------------+
                     │      │       │
                     │      │       │
                     ▼      ▼       ▼
              docker logs  docker exec
                     │
                     ▼
              docker top
                     │
                     ▼
              docker inspect
                     │
                     ▼
              docker stats
                     │
                     ▼
                Healthcheck

---
## Procedimiento

1. Descargar la imagen

Consulte las imágenes disponibles

```bash
docker image ls
```

2. Descargar la imagen

```bash
docker pull hashicorp/http-echo
```

3. Verificar

4. ```bash
docker image ls
```

5. 
