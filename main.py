from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from supabase import create_client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class Account(BaseModel):
    username: str
    email: str
    password: str
    profile_photo: Optional[str] = None

@app.get("/")
def home():
    return {"status": "Accounts API Running"}

@app.get("/accounts")
def get_accounts():
    res = supabase.table("accounts").select("*").execute()
    return res.data

@app.post("/accounts")
def create_account(acc: Account):
    res = supabase.table("accounts").insert(acc.dict()).execute()
    return res.data
