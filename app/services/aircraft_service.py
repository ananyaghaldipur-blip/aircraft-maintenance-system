from sqlalchemy.orm import Session
from app.models import Aircraft

def create_aircraft(db: Session, name: str, model: str):
    aircraft = Aircraft(name=name, model=model)
    db.add(aircraft)
    db.commit()
    db.refresh(aircraft)
    return aircraft


def get_aircraft(db: Session):
    return db.query(Aircraft).all()