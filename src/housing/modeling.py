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
    Carga datos desde data/housing.csv
    """
    csv_path = BASE_DIR / "data" / "housing.csv"
    
    if not csv_path.exists():
        # Fallback de seguridad por si borras el archivo sin querer
        print(f"⚠️ No encuentro {csv_path}. Usando modo sintético de emergencia.")
        # ... aquí podrías poner el código de generación aleatoria si quisieras ...
        raise FileNotFoundError(f"❌ Falta el archivo {csv_path}")

    print(f"🏗️  Leyendo CSV real: {csv_path}")
    df = pd.read_csv(csv_path)
    
    # Solo por seguridad, borramos filas vacías si las hubiera
    df = df.dropna()
    
    print(f"✅ Datos cargados: {len(df)} registros.")
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