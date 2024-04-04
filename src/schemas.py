# app/schemas.py

from pydantic import BaseModel, validator, Field
import re

class CandidateBase(BaseModel):

    dni: str = Field(..., description="El DNI del candidato.")
    nombre: str = Field(..., description="El nombre del candidato.")
    apellido: str = Field(..., description="El apellido del candidato.")

    class Config:
        orm_mode = True

    @validator('dni')
    def validate_dni(cls,value):

        # Patron del DNI español
        pattern = r"^\d{8}[A-Z]$"

        if not re.match(pattern,value):
            raise ValueError('El DNI debe estar compuesto por 8 dígitos seguidos por una letra mayúscula')
        return value

    @validator('nombre','apellido')
    def validate_name(cls, value):

        if not value.replace(" ","").isalpha():
            raise ValueError('Solo debe contener letras y espacios')
        if not 1 < len(value) < 50:
            raise ValueError('La longitud debe estar entre 2 y 50 caracteres')
        return value

# Esquema para solicitudes de creación, donde todos los campos son obligatorios
class CandidateCreate(CandidateBase):
    pass

# Esquema para leer datos, incluyendo el ID y cualquier otro dato relevante
class CandidateRead(CandidateBase):
    pass
