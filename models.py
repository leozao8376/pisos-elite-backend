from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    numero = Column(String)
    cidade = Column(String)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    midias = relationship("Midia", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")
    curtidas = relationship("Curtida", back_populates="usuario")
    orcamentos = relationship("Orcamento", back_populates="usuario")


class Midia(Base):
    __tablename__ = "midias"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(Text)
    tipo = Column(String, nullable=False)  # video ou foto
    url = Column(String, nullable=False)
    thumb = Column(String)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="midias")

    comentarios = relationship("Comentario", back_populates="midia")
    curtidas = relationship("Curtida", back_populates="midia")


class Curtida(Base):
    __tablename__ = "curtidas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    midia_id = Column(Integer, ForeignKey("midias.id"))
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    usuario = relationship("Usuario", back_populates="curtidas")
    midia = relationship("Midia", back_populates="curtidas")

    __table_args__ = (
        UniqueConstraint("usuario_id", "midia_id", name="uq_usuario_midia"),
    )


class Comentario(Base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    midia_id = Column(Integer, ForeignKey("midias.id"))
    texto = Column(Text, nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    usuario = relationship("Usuario", back_populates="comentarios")
    midia = relationship("Midia", back_populates="comentarios")


class Orcamento(Base):
    __tablename__ = "orcamentos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_piso = Column(String)
    metragem = Column(Float)
    preco_calculado = Column(Float)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    usuario = relationship("Usuario", back_populates="orcamentos")