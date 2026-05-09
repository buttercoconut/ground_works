"""SQLAlchemy models for Boring.

Includes Pydantic schemas for request/response.
"""

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from datetime import date

from backend.main import Base

class Boring(Base):
    __tablename__ = "borings"

    id = Column(Integer, primary_key=True, index=True)
    site_name = Column(String, nullable=False)
    depth = Column(Float, nullable=False)
    date_bored = Column(Date, nullable=False)
    notes = Column(String, nullable=True)

    # Relationship to SoilLayer (not defined here for brevity)
    soil_layers = relationship("SoilLayer", back_populates="boring")

# Pydantic schemas
class BoringBase(BaseModel):
    site_name: str = Field(..., example="Site A")
    depth: float = Field(..., example=120.5)
    date_bored: date = Field(..., example="2023-08-15")
    notes: str | None = None

class BoringCreate(BoringBase):
    pass

class BoringRead(BoringBase):
    id: int

    class Config:
        orm_mode = True
