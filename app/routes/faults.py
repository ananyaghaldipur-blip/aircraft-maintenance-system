from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Fault
from app.schemas import FaultCreate, FaultResponse, FaultUpdate

router = APIRouter(prefix="/faults", tags=["Faults"])


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
# CREATE FAULT
# =========================
@router.post("/", response_model=FaultResponse)
def create_fault(data: FaultCreate, db: Session = Depends(get_db)):
    fault = Fault(
        aircraft_id=data.aircraft_id,
        issue=data.issue,
        status=data.status
    )

    db.add(fault)
    db.commit()
    db.refresh(fault)
    return fault


# =========================
# GET ALL FAULTS
# =========================
@router.get("/", response_model=list[FaultResponse])
def get_faults(db: Session = Depends(get_db)):
    return db.query(Fault).all()


# =========================
# GET FAULTS BY AIRCRAFT
# =========================
@router.get("/aircraft/{aircraft_id}", response_model=list[FaultResponse])
def get_faults_by_aircraft(aircraft_id: int, db: Session = Depends(get_db)):
    return db.query(Fault).filter(Fault.aircraft_id == aircraft_id).all()


# =========================
# UPDATE FAULT STATUS
# =========================
@router.patch("/{fault_id}", response_model=FaultResponse)
def update_fault(
    fault_id: int,
    data: FaultUpdate,
    db: Session = Depends(get_db)
):
    fault = db.query(Fault).filter(Fault.id == fault_id).first()

    if not fault:
        raise HTTPException(status_code=404, detail="Fault not found")

    fault.status = data.status

    db.commit()
    db.refresh(fault)
    return fault