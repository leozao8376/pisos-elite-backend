from app.database import Base, engine
from app import models

print("Criando as tabelas...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")