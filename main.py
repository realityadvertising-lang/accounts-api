from fastapi import FastAPI
from supabase import create_client
import os

app = FastAPI()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def home():
    return {"status": "Accounts API Running"}

@app.get("/accounts")
def get_accounts():
    data = supabase.table("accounts").select("*").execute()
    return data.data

@app.post("/accounts")
def create_account(name: str, balance: float = 0):
    data = supabase.table("accounts").insert({"name": name, "balance": balance}).execute()
    return data.data
