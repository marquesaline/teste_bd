from sqlmodel import SQLModel, Field
from typing import Optional

# Definindo um modelo simples usando SQLModel
class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
