from fastapi import APIRouter
from app.database import get_db
from app.schemas import MidiaBase

router = APIRouter()

@router.post("/midias")
def adicionar_midia(midia: MidiaBase):
    db = get_db()
    db.execute("INSERT INTO midias (titulo, descricao, tipo, url, thumb) VALUES (?, ?, ?, ?, ?)",
               (midia.titulo, midia.descricao, midia.tipo, midia.url, midia.thumb))
    db.commit()
    return {"msg": "Mídia adicionada"}