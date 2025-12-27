import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from src.housing.schemas import HouseInput, PredictionOutput

# 1. Definimos el ciclo de vida (Cargar modelo al arrancar)
model_cache = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Ubicamos el archivo (subimos 3 niveles desde main.py hasta la raíz)
    base_dir = Path(__file__).resolve().parent.parent.parent
    model_path = base_dir / "artifacts" / "housing_model.pkl"
    
    # 2. Intentamos cargar
    if model_path.exists():
        print(f"🏗️ Cargando modelo desde: {model_path}")
        model_cache["model"] = joblib.load(model_path)
        print("✅ Modelo cargado en memoria.")
    else:
        # Esto explica el error 503: Si el archivo no está, la API arranca pero vacía.
        print(f"⚠️ ALERTA: No se encontró el modelo en {model_path}")
        print("   Ejecuta 'uv run python src/housing/modeling.py' para generarlo.")
    
    yield
    model_cache.clear()

app = FastAPI(title="Housing API", lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "0.1.0"}



# 3. El Endpoint Nuevo (Lo que pide el test)
@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: HouseInput):
    if "model" not in model_cache:
        raise HTTPException(status_code=503, detail="Modelo no cargado (Ejecuta el entrenamiento primero)")
    
    input_df = pd.DataFrame([input_data.model_dump()])
    
    prediction = model_cache["model"].predict(input_df)
    return {"predicted_price": prediction[0]}