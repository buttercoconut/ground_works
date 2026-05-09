"""SQLAlchemy models for Boring domain."""

from datetime import datetime
from typing import List

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base

class Boring(Base):
    __tablename__ = "borings"

    id = Column(Integer, primary_key=True, index=True)
    site_name = Column(String, nullable=False)
    depth = Column(Float, nullable=False)
    sample_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String, nullable=True)

    layers = relationship("SoilLayer", back_populates="boring", cascade="all, delete-orphan")

class SoilLayer(Base):
    __tablename__ = "soil_layers"

    id = Column(Integer, primary_key=True, index=True)
    boring_id = Column(Integer, ForeignKey("borings.id"), nullable=False)
    depth_start = Column(Float, nullable=False)
    depth_end = Column(Float, nullable=False)
    material = Column(String, nullable=False)
    density = Column(Float, nullable=True)

    boring = relationship("Boring", back_populates="layers")

# Pydantic schemas
from pydantic import BaseModel, Field

class SoilLayerCreate(BaseModel):
    depth_start: float
    depth_end: float
    material: str
    density: float | None = None

class SoilLayerRead(SoilLayerCreate):
    id: int

    class Config:
        orm_mode = True

class BoringCreate(BaseModel):
    site_name: str
    depth: float
    sample_date: datetime | None = None
    notes: str | None = None
    layers: List[SoilLayerCreate] | None = None

class BoringRead(BoringCreate):
    id: int
    layers: List[SoilLayerRead] | None = None

    class Config:
        orm_mode = True

class BoringUpdate(BaseModel):
    site_name: str | None = None
    depth: float | None = None
    sample_date: datetime | None = None
    notes: str | None = None
    layers: List[SoilLayerCreate] | None = None
