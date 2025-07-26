from fastapi import APIRouter, Depends
from app.database import get_db
from app.schemas import UsuarioBase

router = APIRouter()

@router.post("/usuarios")
def criar_usuario(usuario: UsuarioBase):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO usuarios (nome, numero, cidade) VALUES (?, ?, ?)",
                   (usuario.nome, usuario.numero, usuario.cidade))
    db.commit()
    return {"msg": "Usuário criado com sucesso"}