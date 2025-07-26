from fastapi import APIRouter
from app.database import get_db
from app.schemas import CurtidaBase

router = APIRouter()

@router.post("/curtidas")
def curtir(curtida: CurtidaBase):
    db = get_db()
    try:
        db.execute("INSERT INTO curtidas (usuario_id, midia_id) VALUES (?, ?)",
                   (curtida.usuario_id, curtida.midia_id))
        db.commit()
        return {"msg": "Curtida salva"}
    except:
        return {"msg": "Usuário já curtiu essa mídia"}