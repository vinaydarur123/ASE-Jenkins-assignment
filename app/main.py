from fastapi import FastAPI, HTTPException
from app.schemas import UserCreate, UserLogin
from app.auth import create_user, authenticate_user

app = FastAPI()

@app.post("/register")
def register(user: UserCreate):
    if not create_user(user.username, user.password):
        raise HTTPException(status_code=400, detail="User already exists.")
    return {"message": "User registered"}

@app.post("/login")
def login(user: UserLogin):
    if not authenticate_user(user.username, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    return {"message": "Login successful"}
