"""Service layer for Boring.

Encapsulates business logic and database interactions.
"""

from sqlalchemy.orm import Session
from typing import List

from backend.models.boring import Boring, BoringCreate, BoringRead

class BoringService:
    def __init__(self, db: Session):
        self.db = db

    def create_boring(self, boring_in: BoringCreate) -> BoringRead:
        boring = Boring(**boring_in.dict())
        self.db.add(boring)
        self.db.commit()
        self.db.refresh(boring)
        return boring

    def list_borings(self) -> List[BoringRead]:
        return self.db.query(Boring).all()

    def get_boring(self, boring_id: int) -> Boring | None:
        return self.db.query(Boring).filter(Boring.id == boring_id).first()

    def update_boring(self, boring_id: int, boring_in: BoringCreate) -> Boring | None:
        boring = self.get_boring(boring_id)
        if not boring:
            return None
        for key, value in boring_in.dict().items():
            setattr(boring, key, value)
        self.db.commit()
        self.db.refresh(boring)
        return boring

    def delete_boring(self, boring_id: int) -> bool:
        boring = self.get_boring(boring_id)
        if not boring:
            return False
        self.db.delete(boring)
        self.db.commit()
        return True
