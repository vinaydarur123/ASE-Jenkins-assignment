from passlib.context import CryptContext
from app.models import fake_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_user(username: str, password: str):
    if username in fake_db:
        return False
    fake_db[username] = hash_password(password)
    return True

def authenticate_user(username: str, password: str) -> bool:
    hashed = fake_db.get(username)
    if not hashed:
        return False
    return verify_password(password, hashed)
