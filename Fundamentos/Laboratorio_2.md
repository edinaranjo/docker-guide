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
