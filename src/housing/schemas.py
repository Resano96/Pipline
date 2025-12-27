from pydantic import BaseModel, Field, ConfigDict

# Input: Los datos que el cliente nos envía
class HouseInput(BaseModel):
    # En Pydantic V2, los ejemplos van dentro de json_schema_extra
    MedInc: float = Field(..., json_schema_extra={"example": 3.5}, description="Ingreso medio")
    HouseAge: float = Field(..., json_schema_extra={"example": 25.0}, description="Edad de la casa")
    AveRooms: float = Field(..., json_schema_extra={"example": 5.0}, description="Habitaciones promedio")
    AveBedrms: float = Field(..., json_schema_extra={"example": 1.0}, description="Dormitorios promedio")
    Population: float = Field(..., json_schema_extra={"example": 800.0}, description="Población")
    AveOccup: float = Field(..., json_schema_extra={"example": 3.0}, description="Ocupación promedio")
    Latitude: float = Field(..., json_schema_extra={"example": 34.0}, description="Latitud")
    Longitude: float = Field(..., json_schema_extra={"example": -118.0}, description="Longitud")

# Output: Lo que respondemos
class PredictionOutput(BaseModel):
    predicted_price: float