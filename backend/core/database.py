"""Database utilities for the Ground Works backend.

Creates a SQLAlchemy engine and a session factory.  The ``get_db`` dependency
is used by FastAPI to provide a session per request.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_engine(settings.DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI dependency
from fastapi import Depends


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
