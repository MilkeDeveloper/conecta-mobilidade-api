from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import os

load_dotenv()

# Ambiente de teste (CI)
if "GITHUB_ACTIONS" in os.environ:
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
else:
    DATABASE_URL = os.getenv("DATABASE_URL")  # Neon/Render em produção

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# importante para evitar circular imports
Base.metadata.create_all(bind=engine) # isso vai criar a tabela se ela não existir