import os
import platform
import socket
import time
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="DevOps Final Project API",
    description="Aplicación final para construcción de imágenes Docker con buenas prácticas.",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

START_TIME = time.time()

GROUP_NAME = os.getenv("GROUP_NAME", "Grupo no definido")
GROUP_MEMBERS = os.getenv("GROUP_MEMBERS", "Integrantes no definidos")
COURSE_NAME = os.getenv("COURSE_NAME", "Curso de Profesionalización en DevOps")
APP_ENV = os.getenv("APP_ENV", "production")


@app.get("/")
def home(request: Request):
    uptime_seconds = round(time.time() - START_TIME, 2)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "group_name": GROUP_NAME,
            "group_members": GROUP_MEMBERS,
            "course_name": COURSE_NAME,
            "app_env": APP_ENV,
            "uptime_seconds": uptime_seconds,
            "hostname": socket.gethostname(),
            "system": platform.system(),
            "python_version": platform.python_version()
        }
    )


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "devops-final-project",
        "group": GROUP_NAME,
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/info")
def info():
    return {
        "application": "DevOps Final Project API",
        "version": "1.0.0",
        "environment": APP_ENV,
        "group": {
            "name": GROUP_NAME,
            "members": GROUP_MEMBERS
        },
        "system": {
            "hostname": socket.gethostname(),
            "platform": platform.system(),
            "python_version": platform.python_version()
        }
    }


@app.get("/metrics")
def metrics():
    uptime_seconds = round(time.time() - START_TIME, 2)

    return {
        "service": "devops-final-project",
        "uptime_seconds": uptime_seconds,
        "status": "running",
        "group": GROUP_NAME
    }
    
