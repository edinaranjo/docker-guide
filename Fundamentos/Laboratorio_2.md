# 🐳 Laboratorio 2 Monitoreo y Validación Operacional de Contenedores con Grafana
## Objetivos

Al finalizar esta práctica el estudiante será capaz de:

>- Desplegar una aplicación real utilizando Docker.
>- Configurar y analizar un Healthcheck.
>- Interpretar el estado operacional de un contenedor.
>- Analizar el consumo de recursos mediante docker stats.
>- Inspeccionar procesos y configuración del contenedor.
>- Realizar pruebas de conectividad HTTP para validar el servicio.

## Escenario

En este laboratorio se desplegará una instancia de Grafana en un contenedor Docker.

Posteriormente se verificará su disponibilidad mediante un Healthcheck, se analizará el comportamiento del contenedor bajo carga y se inspeccionarán sus recursos internos.

## Arquitectura
                   Cliente

                      │

      curl / Navegador / wget

                      │

               localhost:3000

                      │

          +----------------------+
          |     GRAFANA          |
          | Docker Container     |
          +----------------------+
            │     │      │
            │     │      │
            ▼     ▼      ▼
        Health  Stats  Inspect


---

##Paso 1. Descargar la imagen

```bash
docker pull grafana/grafana
```

Verificar
```bash
docker image ls
```

## Paso 2. Crear el contenedor

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
---
## Paso 3. Verificar el estado

Consultar
```bash
docker ps
```

Esperar aproximadamente un minuto.

El resultado esperado será

STATUS
```bash
Up 1 minute (healthy)
```
---
##  Paso 4. Analizar el Healthcheck

Consultar únicamente el estado.

```bash
docker inspect \
--format='{{.State.Health.Status}}' \
grafana-lab
```
Debe responder
```bash
healthy
```

Consultar el historial.
```bash
docker inspect \
--format='{{json .State.Health}}' \
grafana-lab
```
Analizar:

Status
ExitCode
FailingStreak
Historial de verificaciones

---

## Paso 5. Acceder a Grafana

Abrir
```bash
http://localhost:3000
```

Credenciales

>- Usuario: admin

>- Contraseña: admin

Cambiar la contraseña cuando Grafana lo solicite.
---
## Paso 6. Verificar conectividad HTTP

Desde otra terminal ejecutar

```bash
curl http://localhost:3000/api/health
```
Resultado esperado
```bash
{
  "commit":"...",
  "database":"ok",
  "version":"..."
}
```
Verificar únicamente el código HTTP
```bash

curl -I http://localhost:3000
```
Debe responder

```bash
HTTP/1.1 302 Found
```
## Paso 7. Generar tráfico

Abrir varias pestañas del navegador.

Realizar las siguientes acciones:

>- iniciar sesión
>- refrescar el Dashboard
>- abrir Administration
>- abrir Configuration
>- volver al Home

Mientras tanto ejecutar
```bash
docker stats
```

Analizar

>- CPU
>- MEM
>- NET I/O

---
## Paso 8. Inspeccionar el contenedor

Consultar
```bash
docker inspect grafana-lab
```

Identificar:

>- Dirección IP
>- Imagen utilizada
>- Variables de entorno
>- Redes
>- Puertos publicados

Consultar únicamente la IP

```bash
docker inspect \
-f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
grafana-lab
```
## Paso 9. Analizar procesos

Mostrar los procesos activos.
```bash
docker top grafana-lab
```
---
## Paso 10. Consultar registros

Mostrar los registros.
```bash
docker logs grafana-lab
```
Posteriormente

```bash
docker logs -tf grafana-lab
```
Actualizar el navegador.

Observar las nuevas conexiones.

Salir con Ctrl+C
---
## Paso 11. Simular un fallo del Healthcheck

Crear un segundo contenedor.
```bash
docker run -d \
--name grafana-error \
-p 3001:3000 \
--health-cmd="wget --spider -q http://localhost:3000/noexiste || exit 1" \
--health-interval=10s \
--health-retries=2 \
grafana/grafana
```
Esperar aproximadamente un minuto.

Consultar
```bash
docker ps
```
Comparar

grafana-lab

STATUS

healthy

-----------------------

grafana-error

STATUS

unhealthy

Verificar

```bash
docker inspect \
--format='{{.State.Health.Status}}' \
grafana-error
```

Resultado esperado

unhealthy
---
## Paso 12. Finalizar la práctica

Detener ambos contenedores.
```bash
docker stop grafana-lab grafana-error
```
Eliminar
```bash
docker rm grafana-lab grafana-error
```
