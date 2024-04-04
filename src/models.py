# app/models.py
import sqlalchemy
from .database import Base

class Candidate(Base):
    __tablename__ = 'candidatos'
    
    dni = sqlalchemy.Column(sqlalchemy.String, primary_key=True, index=True)
    nombre = sqlalchemy.Column(sqlalchemy.String)
    apellido = sqlalchemy.Column(sqlalchemy.String)