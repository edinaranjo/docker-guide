# ⚙️ Creación de contenedores a partir de una imagen

```bash
docker run - it --name <container-name> -p <host-port>:<container-port> -d <image-name >
```
---
# ⚙️ Salida Interactiva
```bash
docker run -it <image-name>
```
---

# ⚙️ Ejecutar un contenedor en segundo plano
```bash
docker run -d <image-name>
```
## Ejemplo:

```bash
docker run -d --name miweb -p 8080:80 nginx
```
> - docker run → crea y ejecuta un contenedor.
> - -d → lo ejecuta en modo desacoplado (segundo plano).
> - --name miweb → le da un nombre al contenedor.
> - -p 8080:80 → mapea el puerto 80 del contenedor al puerto 8080 de tu m ´aquina.
> - nginx → usa la imagen oficial de Nginx.

---
# ⚙️ Acceso a contenedores

## Para acceder al contenedor o ejecutar comandos en el mismo:

```bash
docker exec -it <container-name|id> <command>
```

# ⚙️ Healthcheck

```bash
docker run -d --name miweb -p 8080:80 \
--health-cmd="curl -f http://localhost/ || exit 1" \
--health-interval=30s \
--health-retries=3 \
nginx
```

