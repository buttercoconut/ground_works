"""FastAPI application entry point for the Ground Works backend.

This module sets up the FastAPI app, includes routers, configures the database
connection, and starts the Celery worker when the application is run as a
stand‑alone process.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .core.database import engine, Base
from .api import router as api_router

# Create the FastAPI instance
app = FastAPI(
    title="Ground Works API",
    description="API for managing boring tasks and ground works data.",
    version="0.1.0",
)

# Allow CORS for local dev (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router, prefix="/api")

# Create database tables on startup
@app.on_event("startup")
async def on_startup():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

# Optional: expose a health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# If this file is executed directly, start the uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("ground_works.backend.main:app", host="0.0.0.0", port=8000, reload=True)
