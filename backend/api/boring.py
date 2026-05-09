"""API router for Boring operations."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models.boring import BoringCreate, BoringRead, BoringUpdate
from ..services.boring_service import BoringService
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=BoringRead, status_code=status.HTTP_201_CREATED)
def create_boring(boring_in: BoringCreate, db: Session = Depends(get_db)):
    service = BoringService(db)
    return service.create_boring(boring_in)

@router.get("/{boring_id}", response_model=BoringRead)
def read_boring(boring_id: int, db: Session = Depends(get_db)):
    service = BoringService(db)
    boring = service.get_boring(boring_id)
    if not boring:
        raise HTTPException(status_code=404, detail="Boring not found")
    return boring

@router.put("/{boring_id}", response_model=BoringRead)
def update_boring(boring_id: int, boring_in: BoringUpdate, db: Session = Depends(get_db)):
    service = BoringService(db)
    boring = service.update_boring(boring_id, boring_in)
    if not boring:
        raise HTTPException(status_code=404, detail="Boring not found")
    return boring

@router.delete("/{boring_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_boring(boring_id: int, db: Session = Depends(get_db)):
    service = BoringService(db)
    success = service.delete_boring(boring_id)
    if not success:
        raise HTTPException(status_code=404, detail="Boring not found")
    return None
