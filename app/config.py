from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv


#importa o modulo para interagir com o sistema operacional e
#load_dotenv do pacote python-dotenv para carregar as variáveis de ambiente de um arquivo .env.
load_dotenv(dotenv_path=".env.prod")

#Acessa e armazena as variaveis de ambiente específica (Credênciais do banco)
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

#Constrói a URL de conexão com banco de dados a partir das variáveis de ambiente; 
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#Cria um motor de banco de dados SQLAlchemy que gerencia as conexões com banco de dados;
engine = create_engine(DATABASE_URL)

#Cria uma classe base declarativa para os modelos SQLAlchemy
Session_local = sessionmaker(bind=engine, autoflush = False, autocommit = False)

Base = declarative_base()

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close

