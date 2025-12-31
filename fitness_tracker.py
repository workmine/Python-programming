from fastapi import FastAPI, APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import List, Optional
import uuid
from datetime import datetime, timezone, timedelta
import bcrypt
import jwt

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 

security = HTTPBearer()

app = FastAPI()
api_router = APIRouter(prefix="/api")

# ===== MODELS =====
class User(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    user: User

class FitnessEntry(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    date: str
    steps: Optional[int] = 0
    calories: Optional[int] = 0
    distance: Optional[float] = 0.0  
    active_minutes: Optional[int] = 0
    heart_rate: Optional[int] = 0
    sleep_hours: Optional[float] = 0.0
    water_intake: Optional[float] = 0.0  
    weight: Optional[float] = 0.0  
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class FitnessEntryCreate(BaseModel):
    date: str
    steps: Optional[int] = 0
    calories: Optional[int] = 0
    distance: Optional[float] = 0.0
    active_minutes: Optional[int] = 0
    heart_rate: Optional[int] = 0
    sleep_hours: Optional[float] = 0.0
    water_intake: Optional[float] = 0.0
    weight: Optional[float] = 0.0

class WorkoutEntry(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    date: str
    workout_type: str
    duration: int  
    calories_burned: int
    notes: Optional[str] = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class WorkoutEntryCreate(BaseModel):
    date: str
    workout_type: str
    duration: int
    calories_burned: int
    notes: Optional[str] = ""

# ===== HELPER FUNCTIONS =====
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ===== AUTH ROUTES =====
@api_router.post("/auth/signup", response_model=TokenResponse)
async def signup(user_data: UserCreate):
    existing_user = await db.users.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_obj = User(email=user_data.email, name=user_data.name)
    user_dict = user_obj.model_dump()
    user_dict['created_at'] = user_dict['created_at'].isoformat()
    user_dict['password'] = hash_password(user_data.password)
    
    await db.users.insert_one(user_dict)
    
    access_token = create_access_token(data={"sub": user_obj.id})
    
    return TokenResponse(access_token=access_token, user=user_obj)

@api_router.post("/auth/login", response_model=TokenResponse)
async def login(login_data: UserLogin):
    user = await db.users.find_one({"email": login_data.email})
    if not user or not verify_password(login_data.password, user['password']):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    if isinstance(user['created_at'], str):
        user['created_at'] = datetime.fromisoformat(user['created_at'])
    
    user_obj = User(**user)
    access_token = create_access_token(data={"sub": user_obj.id})
    
    return TokenResponse(access_token=access_token, user=user_obj)

@api_router.get("/auth/me", response_model=User)
async def get_me(user_id: str = Depends(get_current_user)):
    user = await db.users.find_one({"id": user_id}, {"_id": 0, "password": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if isinstance(user['created_at'], str):
        user['created_at'] = datetime.fromisoformat(user['created_at'])
    
    return User(**user)

# ===== FITNESS ENTRY ROUTES =====
@api_router.post("/fitness-entries", response_model=FitnessEntry)
async def create_fitness_entry(entry_data: FitnessEntryCreate, user_id: str = Depends(get_current_user)):
    existing = await db.fitness_entries.find_one({"user_id": user_id, "date": entry_data.date})
    if existing:
        raise HTTPException(status_code=400, detail="Entry for this date already exists. Please update instead.")
    
    entry_obj = FitnessEntry(user_id=user_id, **entry_data.model_dump())
    entry_dict = entry_obj.model_dump()
    entry_dict['created_at'] = entry_dict['created_at'].isoformat()
    
    await db.fitness_entries.insert_one(entry_dict)
    return entry_obj

@api_router.get("/fitness-entries", response_model=List[FitnessEntry])
async def get_fitness_entries(user_id: str = Depends(get_current_user), limit: int = 30):
    entries = await db.fitness_entries.find(
        {"user_id": user_id}, 
        {"_id": 0}
    ).sort("date", -1).limit(limit).to_list(limit)
    
    for entry in entries:
        if isinstance(entry['created_at'], str):
            entry['created_at'] = datetime.fromisoformat(entry['created_at'])
    
    return [FitnessEntry(**entry) for entry in entries]

@api_router.put("/fitness-entries/{entry_id}", response_model=FitnessEntry)
async def update_fitness_entry(
    entry_id: str, 
    entry_data: FitnessEntryCreate, 
    user_id: str = Depends(get_current_user)
):
    entry = await db.fitness_entries.find_one({"id": entry_id, "user_id": user_id})
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    
    update_data = entry_data.model_dump()
    await db.fitness_entries.update_one(
        {"id": entry_id, "user_id": user_id},
        {"$set": update_data}
    )
    
    updated_entry = await db.fitness_entries.find_one({"id": entry_id}, {"_id": 0})
    if isinstance(updated_entry['created_at'], str):
        updated_entry['created_at'] = datetime.fromisoformat(updated_entry['created_at'])
    
    return FitnessEntry(**updated_entry)

@api_router.delete("/fitness-entries/{entry_id}")
async def delete_fitness_entry(entry_id: str, user_id: str = Depends(get_current_user)):
    result = await db.fitness_entries.delete_one({"id": entry_id, "user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"message": "Entry deleted successfully"}

@api_router.post("/workouts", response_model=WorkoutEntry)
async def create_workout(workout_data: WorkoutEntryCreate, user_id: str = Depends(get_current_user)):
    workout_obj = WorkoutEntry(user_id=user_id, **workout_data.model_dump())
    workout_dict = workout_obj.model_dump()
    workout_dict['created_at'] = workout_dict['created_at'].isoformat()
    
    await db.workouts.insert_one(workout_dict)
    return workout_obj

@api_router.get("/workouts", response_model=List[WorkoutEntry])
async def get_workouts(user_id: str = Depends(get_current_user), limit: int = 30):
    workouts = await db.workouts.find(
        {"user_id": user_id}, 
        {"_id": 0}
    ).sort("date", -1).limit(limit).to_list(limit)
    
    for workout in workouts:
        if isinstance(workout['created_at'], str):
            workout['created_at'] = datetime.fromisoformat(workout['created_at'])
    
    return [WorkoutEntry(**workout) for workout in workouts]

@api_router.delete("/workouts/{workout_id}")
async def delete_workout(workout_id: str, user_id: str = Depends(get_current_user)):
    result = await db.workouts.delete_one({"id": workout_id, "user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Workout not found")
    return {"message": "Workout deleted successfully"}

# ===== STATS ROUTE =====
@api_router.get("/stats")
async def get_stats(user_id: str = Depends(get_current_user)):
    entries = await db.fitness_entries.find(
        {"user_id": user_id}, 
        {"_id": 0}
    ).sort("date", -1).limit(7).to_list(7)
    
    total_workouts = await db.workouts.count_documents({"user_id": user_id})
    
    if entries:
        avg_steps = sum(e.get('steps', 0) for e in entries) // len(entries)
        avg_calories = sum(e.get('calories', 0) for e in entries) // len(entries)
        avg_sleep = sum(e.get('sleep_hours', 0) for e in entries) / len(entries)
        total_distance = sum(e.get('distance', 0) for e in entries)
    else:
        avg_steps = avg_calories = avg_sleep = total_distance = 0
    
    return {
        "avg_steps": avg_steps,
        "avg_calories": avg_calories,
        "avg_sleep_hours": round(avg_sleep, 1),
        "total_distance_km": round(total_distance, 1),
        "total_workouts": total_workouts,
        "entries_count": len(entries)
    }

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()