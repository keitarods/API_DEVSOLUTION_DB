from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProdutosSchema(BaseModel):
    g: str
    col1: int
    col2: int
    col3: int
    col4: int
    col5: int
    col6: int
    col7: int
    col8: int
    col9: str