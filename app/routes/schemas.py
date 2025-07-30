from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    numero: str
    cidade: str

class MidiaBase(BaseModel):
    titulo: str
    descricao: str
    tipo: str
    url: str
    thumb: str = None

class ComentarioBase(BaseModel):
    usuario_id: int
    midia_id: int
    texto: str

class CurtidaBase(BaseModel):
    usuario_id: int
    midia_id: int

class OrcamentoBase(BaseModel):
    usuario_id: int
    tipo_piso: str
    metragem: float
    preco_calculado: float