from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class Lead(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    company: Optional[str] = None
    role: Optional[str] = None
    company_size: Optional[str] = None
    industry: Optional[str] = None
    monthly_openings: Optional[str] = None
    current_ats: Optional[str] = None
    bottlenecks: Optional[List[str]] = Field(default_factory=list)
    interests: Optional[List[str]] = Field(default_factory=list)
    channels: Optional[List[str]] = Field(default_factory=list)
    design_partner: Optional[bool] = False
    timezone: Optional[str] = None
    notes: Optional[str] = None
    consent: bool = True
    created_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "email": "jane@acme.com",
                "name": "Jane Doe",
                "company": "Acme Inc",
                "role": "Head of Talent",
                "company_size": "51-200",
                "industry": "SaaS",
                "monthly_openings": "10-20",
                "current_ats": "Greenhouse",
                "bottlenecks": ["Scheduling", "Screening"],
                "interests": ["Automation", "Candidate Portal", "Reporting"],
                "channels": ["Email", "WhatsApp"],
                "design_partner": True,
                "timezone": "UTC+1",
                "notes": "Looking for beta in Q1",
                "consent": True,
            }
        }
