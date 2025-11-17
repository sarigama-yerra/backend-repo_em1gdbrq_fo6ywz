from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import EmailStr
from typing import List, Optional
from datetime import datetime

from database import db, create_document, get_documents
from schemas import Lead

app = FastAPI(title="ATS Prelaunch API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def test():
    info = await db.command({"ping": 1})
    return {"status": "ok", "db": info}


@app.post("/leads")
async def create_lead(lead: Lead):
    lead_data = lead.dict()
    lead_data["created_at"] = datetime.utcnow()
    inserted = await create_document("lead", lead_data)
    if not inserted:
        raise HTTPException(status_code=500, detail="Failed to create lead")
    return {"success": True, "id": str(inserted)}


@app.get("/leads")
async def list_leads(limit: int = 50, email: Optional[EmailStr] = None):
    filter_dict = {"email": str(email)} if email else {}
    docs = await get_documents("lead", filter_dict=filter_dict, limit=limit)
    return {"items": docs}
