from src.housing.modeling import train_model, ARTIFACTS_DIR

def test_training_pipeline_generates_model():
    """
    Test de Humo (Smoke Test) para la fase de entrenamiento.
    Verifica que:
    1. La función 'train_model' se ejecuta sin romper.
    2. Crea el archivo 'housing_model.pkl' en la carpeta correcta.
    3. El archivo tiene contenido (no está vacío).
    """
    
    # 1. EJECUCIÓN
    # Llamamos a la función de entrenamiento directamente.
    # Si el código tiene un error, el test fallará aquí mismo.
    train_model()

    # 2. INSPECCIÓN DE OBRA (Asserts)
    # Definimos dónde debería estar el modelo
    model_path = ARTIFACTS_DIR / "housing_model.pkl"

    # Verificación A: ¿Existe el archivo?
    assert model_path.exists(), f"❌ El archivo no se ha creado en: {model_path}"
    
    # Verificación B: ¿Tiene contenido? (stat().st_size devuelve el tamaño en bytes)
    # Si pesa 0 bytes, es que algo ha fallado silenciosamente.
    assert model_path.stat().st_size > 0, "❌ El archivo del modelo está vacío (0 bytes)."