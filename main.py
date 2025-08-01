from fastapi import FastAPI
from app.routes import usuarios, midias, comentarios, curtidas, orcamentos

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(midias.router)
app.include_router(comentarios.router)
app.include_router(curtidas.router)
app.include_router(orcamentos.router)

@app.get("/")
def home():
    return {"mensagem": "Backend da Pisos Elite rodando!"}