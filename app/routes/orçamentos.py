from fastapi import APIRouter
from app.database import get_db
from app.schemas import OrcamentoBase

router = APIRouter()

@router.post("/orcamentos")
def criar_orcamento(orcamento: OrcamentoBase):
    db = get_db()
    db.execute("INSERT INTO orcamentos (usuario_id, tipo_piso, metragem, preco_calculado) VALUES (?, ?, ?, ?)",
               (orcamento.usuario_id, orcamento.tipo_piso, orcamento.metragem, orcamento.preco_calculado))
    db.commit()
    return {"msg": "Orçamento salvo"}