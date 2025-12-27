from fastapi.testclient import TestClient
from src.housing.main import app

def test_health_check():
    """
    Verifica que la API está viva y devuelve la versión correcta.
    Usamos 'with' para asegurar que el ciclo de vida (lifespan) se ejecuta.
    """
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        # Verificamos que coincida con lo que pusimos en main.py
        assert response.json() == {"status": "ok", "version": "0.1.0"}

def test_prediction():
    """
    Verifica que la predicción funciona.
    Al usar 'with TestClient', la API cargará el modelo .pkl antes de recibir la petición.
    """
    payload = {
        "MedInc": 3.5,
        "HouseAge": 30.0,
        "AveRooms": 6.0,
        "AveBedrms": 1.0,
        "Population": 800.0,
        "AveOccup": 3.0,
        "Latitude": 34.0,
        "Longitude": -118.0
    }
    
    with TestClient(app) as client:
        response = client.post("/predict", json=payload)
        
        # Si esto falla con 422, es culpa del Schema.
        # Si falla con 503, es culpa de que no encuentra el .pkl
        assert response.status_code == 200, f"Error en la API: {response.text}"
        
        data = response.json()
        assert "predicted_price" in data
        assert isinstance(data["predicted_price"], float)