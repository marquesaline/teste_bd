from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select
from models import Item

# Configurando a URL de conexão com o MySQL
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/test"

# Criando o engine de conexão
engine = create_engine(DATABASE_URL, echo=True)

# Função para criar as tabelas no banco de dados
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

# Inicializando as tabelas no banco ao iniciar o app
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Rota simples para adicionar um item ao banco
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

# Rota para listar todos os itens do banco de dados
@app.get("/items/")
def read_items():
    with Session(engine) as session:
        statement = select(Item)
        results = session.exec(statement)
        items = results.all()
        return items
