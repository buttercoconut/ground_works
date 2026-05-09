"""Service layer for Boring operations."""

from sqlalchemy.orm import Session
from ..models.boring import Boring, BoringCreate, BoringRead, BoringUpdate, SoilLayerCreate

class BoringService:
    def __init__(self, db: Session):
        self.db = db

    def create_boring(self, boring_in: BoringCreate) -> BoringRead:
        boring = Boring(
            site_name=boring_in.site_name,
            depth=boring_in.depth,
            sample_date=boring_in.sample_date,
            notes=boring_in.notes,
        )
        if boring_in.layers:
            for layer_in in boring_in.layers:
                layer = SoilLayerCreate(**layer_in.dict())
                boring.layers.append(layer)
        self.db.add(boring)
        self.db.commit()
        self.db.refresh(boring)
        return boring

    def get_boring(self, boring_id: int) -> BoringRead | None:
        return self.db.query(Boring).filter(Boring.id == boring_id).first()

    def update_boring(self, boring_id: int, boring_in: BoringUpdate) -> BoringRead | None:
        boring = self.db.query(Boring).filter(Boring.id == boring_id).first()
        if not boring:
            return None
        for var, value in boring_in.dict(exclude_unset=True).items():
            if var == "layers":
                # Simplified: replace all layers
                boring.layers.clear()
                for layer_in in value:
                    layer = SoilLayerCreate(**layer_in.dict())
                    boring.layers.append(layer)
            else:
                setattr(boring, var, value)
        self.db.commit()
        self.db.refresh(boring)
        return boring

    def delete_boring(self, boring_id: int) -> bool:
        boring = self.db.query(Boring).filter(Boring.id == boring_id).first()
        if not boring:
            return False
        self.db.delete(boring)
        self.db.commit()
        return True
