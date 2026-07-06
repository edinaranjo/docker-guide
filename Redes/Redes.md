
# 🌐 Guía Profesional: Redes en Docker

Docker no solo aísla procesos en contenedores, sino que también **abstrae la red** para permitir que los contenedores se comuniquen entre sí, con el host y con el mundo exterior de manera segura y eficiente.

---

## 🧐 1. Conceptos Clave

El subsistema de red de Docker permite la interconexión mediante diferentes controladores. La capacidad de comunicación es una de las características más potentes de la plataforma:

*   **Abstracción:** Los contenedores no necesitan conocer la infraestructura física subyacente.
*   **Aislamiento:** Es posible crear redes privadas para que solo ciertos contenedores se vean entre sí.
*   **Resolución DNS:** Docker incluye un servidor DNS interno que permite la comunicación por el **nombre del contenedor** en redes personalizadas.

---

## 🚦 2. Tipos de Redes Disponibles

Existen varios controladores (drivers) de red según la necesidad de conectividad:

| Tipo de Red | Descripción | Caso de Uso |
| :--- | :--- | :--- |
| **Bridge (Puente)** | Red interna predeterminada en el host. Usa NAT para salir a Internet. | Aplicaciones estándar en un solo host. |
| **Host** | El contenedor comparte la pila de red del host sin aislamiento. | Maximizar rendimiento o servicios de red complejos. |
| **Overlay** | Permite comunicación entre contenedores en distintos hosts físicos. | Clústeres con **Docker Swarm**. |
| **Macvlan** | Asigna una MAC e IP directamente en la red física. | Integración con redes heredadas o monitoreo de tráfico físico. |

---

## 🛠️ 3. Administración de Redes

Comandos esenciales para gestionar el entorno de red:

*   🔍 **Listar redes:** `docker network ls`
*   🏗️ **Crear red bridge:** `docker network create --driver bridge mi_red`
*   🔗 **Conectar contenedor:** `docker network connect mi_red mi_contenedor`
*   ✂️ **Desconectar contenedor:** `docker network disconnect mi_red mi_contenedor`
*   🗑️ **Eliminar red:** `docker network rm mi_red`

---

## 🚀 4. Implementación Práctica

### Conectividad en Redes Bridge Personalizadas
Al usar una red creada por el usuario, Docker habilita la resolución de nombres automática:

```bash
# 1. Crear la red
docker network create mi_red_bridge

# 2. Desplegar contenedores en esa red
docker run -dit --name app_web --network mi_red_bridge nginx
docker run -dit --name base_datos --network mi_red_bridge mysql:8

# 3. Probar comunicación por NOMBRE
docker exec -it app_web ping base_datos
```

### Uso de Red Host
Útil cuando el contenedor necesita usar puertos del host directamente sin mapeos `-p`:
```bash
docker run -dit --name mi_servidor --network host nginx
```

---
