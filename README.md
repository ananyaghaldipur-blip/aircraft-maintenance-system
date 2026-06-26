# Aircraft Maintenance System (FastAPI)

## Overview
A backend system for managing aircraft records and fault tracking with authentication and role-based access using JWT.

## Tech Stack
- FastAPI
- SQLAlchemy
- MySQL
- JWT Authentication
- Passlib (bcrypt)
- Uvicorn

## Features
- User registration & login (JWT auth)
- Add aircraft
- Track aircraft faults
- Relational DB (Aircraft ↔ Faults)
- Protected routes using OAuth2

## Project Structure
app/
 ├── auth/
 ├── routes/
 ├── services/
 ├── models.py
 ├── schemas.py
 ├── database.py
 └── main.py

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Setup DB
Create MySQL database:
aircraft_db

Update .env:
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/aircraft_db

### 3. Run server
uvicorn app.main:app --reload

## API Endpoints

### Auth
POST /auth/register
POST /auth/login

### Aircraft
GET /aircraft
POST /aircraft (protected)

### Faults
GET /faults
POST /faults
GET /faults/aircraft/{id}

## Security
JWT-based authentication using OAuth2PasswordBearer