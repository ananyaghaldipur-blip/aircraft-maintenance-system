from dotenv import load_dotenv
load_dotenv()

import logging
import traceback

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.database import Base, engine

# Import ALL models so SQLAlchemy knows about them
from app.models import Aircraft, Fault, User

from app.routes import aircraft, faults
from app.auth import routes as auth


# =========================
# LOGGING SETUP (IMPORTANT)
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger("aircraft-api")


# =========================
# DB INIT
# =========================
Base.metadata.create_all(bind=engine)


# =========================
# FASTAPI APP
# =========================
app = FastAPI()

# Include routers
app.include_router(aircraft.router)
app.include_router(faults.router)
app.include_router(auth.router)


# =========================
# HOME ROUTE
# =========================
@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {"message": "Aircraft Maintenance API is running"}


# =========================
# GLOBAL EXCEPTION HANDLER
# =========================
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    traceback.print_exc()

    logger.error(f"Unhandled error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={"message": str(exc)}
    )