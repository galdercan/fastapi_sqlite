# app/main.py
import asyncio
from fastapi import FastAPI, Depends, HTTPException, Response
from fastapi.responses import JSONResponse

# dependencias
from . import crud, schemas, models
from typing import List


# sqlite
from sqlalchemy.orm import Session
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(

    title="FastAPI - Candidatos",
    description="API para crear/consultar candidatos de  una BD Sqlite",
    version="0.0.1",
    contact={
        "name": "Galder Canduela"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Generar un candidato nuevo
@app.post("/candidato/", response_model=schemas.CandidateRead,tags=["Candidatos"])
async def create_candidate(candidate: schemas.CandidateCreate, db: Session = Depends(get_db)):
    # Comprobar si el candidato ya existe de forma asíncrona
    checkCandidate = await asyncio.to_thread(crud.get_candidate_by_dni, db, candidate.dni)

    if checkCandidate:
        raise HTTPException(status_code=400, detail="El dni ya esta registrado")
    
    # Crear el nuevo candidato de forma asíncrona
    await asyncio.to_thread(crud.create_candidate, db, candidate)

    return JSONResponse(content={"message": "Candidato creado correctamente"}, status_code=201)



#Obtener candidato por dni
@app.get("/candidato/{dni}", response_model=schemas.CandidateRead, tags=["Candidatos"], responses={200: {"model": schemas.CandidateRead}, 404: {"model": str}})
async def read_candidate(dni: str, db: Session = Depends(get_db)):
    
    candidate = await asyncio.to_thread(crud.get_candidate_by_dni, db, dni)

    if candidate is None:
        return JSONResponse(status_code=404, content={"message": "Candidato no encontrado"})
    
    return schemas.CandidateRead.from_orm(candidate)


# Obtener todos los candidatos creados
@app.get("/candidatos/", response_model=List[schemas.CandidateRead], tags=["Candidatos"])
async def read_candidates(db: Session = Depends(get_db)):
    
    candidates = await asyncio.to_thread(crud.get_all_candidates, db)

    if not candidates:
        return JSONResponse(status_code=404, content={"message": "No hay candidatos creados"})

    return [schemas.CandidateRead.from_orm(candidate) for candidate in candidates]