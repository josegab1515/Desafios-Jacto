from pydantic import BaseModel, Field, ValidationError

class CarSchema(BaseModel):
    modelo: str = Field(..., min_length=1, max_length=50)
    ano: int 
    mpg: float 