"""FastAPI application entry point for Ground Works backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from .api.boring import router as boring_router

app = FastAPI(title="Ground Works API", version="0.1.0")

# CORS settings for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(boring_router, prefix="/api/boring", tags=["Boring"])

@app.get("/")
async def root():
    return {"message": "Welcome to Ground Works API"}
