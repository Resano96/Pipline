from pathlib import Path
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Definimos rutas relativas para que funcione en cualquier ordenador
# BASE_DIR será la carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"

def load_data():
    """
    Genera datos sintéticos porque la cantera oficial tiene bloqueo de red.
    Simula el dataset California Housing.
    """
    print("🏗️  Generando datos sintéticos en sitio...")
    
    # Mismas columnas que el original para mantener la estructura
    cols = [
        "MedInc", "HouseAge", "AveRooms", "AveBedrms", 
        "Population", "AveOccup", "Latitude", "Longitude", "MedHouseVal"
    ]
    
    # Generamos 1000 filas aleatorias
    np.random.seed(42)
    data = np.random.rand(1000, 9)
    df = pd.DataFrame(data, columns=cols)
    
    # Ajustes de escala para realismo
    df["MedHouseVal"] = df["MedHouseVal"] * 5
    
    return df

def train_model():
    """
    Pipeline completo de entrenamiento: Carga -> Split -> Entrena -> Guarda
    """
    # 1. Carga
    df = load_data()
    
    # 2. Preparación (Separar X e y)
    X = df.drop("MedHouseVal", axis=1)
    y = df["MedHouseVal"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 3. Entrenamiento (La maquinaria)
    print("🚜 Entrenando modelo de Regresión Lineal...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 4. Evaluación
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"✅ Modelo entrenado. MSE en Test: {mse:.4f}")
    
    # 5. Guardado (Empaquetado del producto final)
    # Creamos la carpeta artifacts si no existe
    ARTIFACTS_DIR.mkdir(exist_ok=True)
    model_path = ARTIFACTS_DIR / "housing_model.pkl"
    
    joblib.dump(model, model_path)
    print(f"💾 Modelo guardado exitosamente en: {model_path}")

if __name__ == "__main__":
    # Este bloque permite que el script se ejecute desde la terminal
    train_model()