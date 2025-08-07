from __future__ import annotations

from sqlalchemy import Column, DateTime, Float, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    numero: Mapped[str | None] = mapped_column(nullable=True)
    cidade: Mapped[str | None] = mapped_column(nullable=True)
    criado_em: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    midias: Mapped[list[Midia]] = relationship(back_populates="usuario")
    comentarios: Mapped[list[Comentario]] = relationship(back_populates="usuario")
    curtidas: Mapped[list[Curtida]] = relationship(back_populates="usuario")
    orcamentos: Mapped[list[Orcamento]] = relationship(back_populates="usuario")


class Midia(Base):
    __tablename__ = "midias"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    titulo: Mapped[str | None] = mapped_column(nullable=True)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    tipo: Mapped[str] = mapped_column(nullable=False)  # video ou foto
    url: Mapped[str] = mapped_column(nullable=False)
    thumb: Mapped[str | None] = mapped_column(nullable=True)
    criado_em: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuario: Mapped[Usuario] = relationship(back_populates="midias")

    comentarios: Mapped[list[Comentario]] = relationship(back_populates="midia")
    curtidas: Mapped[list[Curtida]] = relationship(back_populates="midia")


class Curtida(Base):
    __tablename__ = "curtidas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    midia_id: Mapped[int] = mapped_column(ForeignKey("midias.id"))
    criado_em: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuario: Mapped[Usuario] = relationship(back_populates="curtidas")
    midia: Mapped[Midia] = relationship(back_populates="curtidas")

    __table_args__ = (
        UniqueConstraint("usuario_id", "midia_id", name="uq_usuario_midia"),
    )


class Comentario(Base):
    __tablename__ = "comentarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    midia_id: Mapped[int] = mapped_column(ForeignKey("midias.id"))
    texto: Mapped[str] = mapped_column(Text, nullable=False)
    criado_em: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuario: Mapped[Usuario] = relationship(back_populates="comentarios")
    midia: Mapped[Midia] = relationship(back_populates="comentarios")


class Orcamento(Base):
    __tablename__ = "orcamentos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    tipo_piso: Mapped[str]
    metragem: Mapped[float]
    preco_calculado: Mapped[float]
    criado_em: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    usuario: Mapped[Usuario] = relationship(back_populates="orcamentos")