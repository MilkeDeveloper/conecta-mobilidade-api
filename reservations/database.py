from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import os

# recupera a URL do Neon das variáveis de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# importante para evitar circular imports
Base.metadata.create_all(bind=engine) # isso vai criar a tabela se ela não existir