from fastapi import APIRouter
from app.database import get_db
from app.schemas import ComentarioBase

router = APIRouter()

@router.post("/comentarios")
def comentar(coment: ComentarioBase):
    db = get_db()
    db.execute("INSERT INTO comentarios (usuario_id, midia_id, texto) VALUES (?, ?, ?)",
               (coment.usuario_id, coment.midia_id, coment.texto))
    db.commit()
    return {"msg": "Comentário salvo"}