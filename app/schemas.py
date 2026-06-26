from pydantic import BaseModel


# =========================
# AIRCRAFT SCHEMAS
# =========================

class AircraftCreate(BaseModel):
    name: str
    model: str


class AircraftResponse(BaseModel):
    id: int
    name: str
    model: str

    class Config:
        from_attributes = True


# =========================
# FAULT SCHEMAS
# =========================

class FaultCreate(BaseModel):
    aircraft_id: int
    issue: str
    status: str = "open"


class FaultUpdate(BaseModel):
    status: str


class FaultResponse(BaseModel):
    id: int
    aircraft_id: int
    issue: str
    status: str

    class Config:
        from_attributes = True


# =========================
# USER SCHEMAS
# =========================

class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


# =========================
# AUTH TOKEN
# =========================

class Token(BaseModel):
    access_token: str
    token_type: str