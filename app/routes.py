from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException

from .schema import ProdutosSchema
from .config import Session_local, get_db
from .model import Produto

router = APIRouter()

@router.get("/") #Request
def ola_mundo(): #Response
    return {"Dev":"Soluções"}

@router.get("/obtem_dados", response_model = list[ProdutosSchema])
def listar_produtos(db:Session = Depends(get_db)):
    return db.query(Produto).all() #Select * FROM produtos

@router.post("/inseri_dados", response_model=List[ProdutosSchema])
def inserir_produto(produto: ProdutosSchema, db: Session = Depends(get_db)):
    try:
        # Criando uma instância do modelo SQLAlchemy (Produto)
        db_produto = Produto(**produto.dict())

        # Adicionando ao banco de dados
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)

        # Retornando o objeto criado como dicionário
        return [db_produto.__dict__]
    
    except Exception as e:
        print(f"Erro ao inserir produto: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")

@router.delete("/deleta_dados/{produto_id}", response_model=dict)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return {"message": "Produto removido com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")