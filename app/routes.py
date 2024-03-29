from sqlalchemy.orm import Session
from sqlalchemy.sql import desc
from typing import List
from fastapi import APIRouter, Depends, HTTPException

from .schema import ProdutosSchema, ProdutosSchema2
from .config import Session_local, get_db
from .model import Produto

router = APIRouter()

@router.get("/") #Request
def inicio(): #Response
    return {"Dev":"Soluções"}

@router.get("/obtem_dados", response_model = List[ProdutosSchema])
def listar_produtos(db:Session = Depends(get_db)):
    produtos =  db.query(Produto).all() #Select * FROM produtos
    produtos_dict = [produto.__dict__ for produto in produtos]
    return produtos_dict

@router.get("/obtem_ultimo", response_model = List[ProdutosSchema])
def listar_produtos2(db:Session = Depends(get_db)):
    produtos =  db.query(Produto).order_by(desc(Produto.id)).first()
    produtos_dict = [produtos.__dict__] #SELECT * FROM produtos ORDER BY id DESC LIMIT 1
    return produtos_dict

@router.post("/inseri_dados", response_model=List[ProdutosSchema])
def inserir_produto(produto: ProdutosSchema2, db: Session = Depends(get_db)):
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