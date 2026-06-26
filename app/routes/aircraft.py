from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import AircraftCreate, AircraftResponse
from app.services.aircraft_service import create_aircraft, get_aircraft
from app.auth.dependencies import get_current_user

router = APIRouter()


# =========================
# DB DEPENDENCY
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# CREATE AIRCRAFT (PROTECTED)
# =========================
@router.post("/aircraft", response_model=AircraftResponse)
def create_aircraft_route(
    data: AircraftCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)   # 🔐 AUTH REQUIRED
):
    return create_aircraft(db, data.name, data.model)


# =========================
# GET ALL AIRCRAFT (PROTECTED)
# =========================
@router.get("/aircraft", response_model=list[AircraftResponse])
def get_aircraft_route(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)   # 🔐 AUTH REQUIRED
):
    return get_aircraft(db)