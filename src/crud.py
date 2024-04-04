# app/crud.py
from sqlalchemy.orm import Session

from . import models, schemas

def create_candidate(db: Session, candidate: schemas.CandidateCreate):
    db_candidate = models.Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

def get_candidate_by_dni(db: Session, dni: str):
    return db.query(models.Candidate).filter(models.Candidate.dni == dni).first()

def get_all_candidates(db: Session):
    return db.query(models.Candidate).all()
