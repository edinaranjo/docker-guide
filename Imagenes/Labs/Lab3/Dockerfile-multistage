#Dockerfile-multistage
# ======================
# Etapa 1: Build
# ======================
FROM gcc:12 AS builder
WORKDIR /src
# Copiamos el codigo fuente
COPY hello.c .
# Compilamos el binario estatico
RUN gcc -static -o hello hello.c

# ======================
# Etapa 2: Runtime
# ======================
FROM alpine:latest
WORKDIR /app
# Copiamos SOLO el binario desde builder
COPY --from=builder /src/hello .
# Comando por defecto
CMD ["./hello"]
