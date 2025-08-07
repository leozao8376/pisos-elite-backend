from pydantic import BaseModel
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str
    numero: Optional[str] = None
    cidade: Optional[str] = None


class MidiaBase(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    tipo: str
    url: str
    thumb: Optional[str] = None
    usuario_id: int


class ComentarioBase(BaseModel):
    texto: str
    usuario_id: int
    midia_id: int


class CurtidaBase(BaseModel):
    usuario_id: int
    midia_id: int


class OrcamentoBase(BaseModel):
    usuario_id: int
    tipo_piso: str
    metragem: float
    preco_calculado: float