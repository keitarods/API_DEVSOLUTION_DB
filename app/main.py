from fastapi import FastAPI
from .schema import ProdutosSchema
from .routes import router
from typing import List

app = FastAPI()

app.include_router(router)