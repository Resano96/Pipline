# --- FASE 1: Builder (La Hormigonera) ---
# Usamos Python 3.13 Slim como base
FROM python:3.13-slim AS builder

# Instalamos 'uv' copiándolo directamente desde su imagen oficial (truco de experto)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 1. Copiamos SOLO los archivos de requisitos primero
# Esto permite a Docker usar la caché. Si no cambias dependencias, este paso se salta.
COPY pyproject.toml uv.lock ./

# 2. Instalamos las dependencias
# --frozen: Usa versiones exactas del uv.lock (seguridad total)
# --no-dev: No instala pytest ni ruff (ahorramos espacio en producción)
RUN uv sync --frozen --no-dev

# --- FASE 2: Runtime (El Edificio Final) ---
# Empezamos de cero con una imagen limpia y ligera
FROM python:3.13-slim

# Definimos el directorio de trabajo
WORKDIR /app

# 1. Copiamos el entorno virtual (.venv) generado en la Fase 1
# Fíjate que lo traemos desde "--from=builder"
COPY --from=builder /app/.venv /app/.venv

# 2. Activamos el entorno virtual automáticamente
# Añadimos la carpeta bin del venv al PATH del sistema
ENV PATH="/app/.venv/bin:$PATH"

# 3. Copiamos el código fuente de la aplicación
COPY src ./src

# 4. Copiamos el modelo entrenado (artifacts)
# IMPORTANTE: Docker asume que ya ejecutaste 'modeling.py' en tu local
COPY artifacts ./artifacts

# 5. Comando de arranque
# Ejecuta Uvicorn escuchando en el puerto 80 (estándar de contenedores)
CMD ["uvicorn", "src.housing.main:app", "--host", "0.0.0.0", "--port", "80"]