from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Producao (BaseModel):
    produto: str    
    quantidade: int | None

class ListProducao(BaseModel):
    producoes: list[Producao]

class Processamento(BaseModel):
    cultivar: str
    quantidade: int | None
    sclaissificacao: str

class ListProcessamento(BaseModel):
    processamento:list[Processamento]

class Comercializacao(BaseModel):    
    produto: str
    quantidade: int | None

class ListComercializao(BaseModel):
    comercializacao:list[Comercializacao]

class Importacao(BaseModel):
    paises: str
    quantidade: int | None
    valor: int | None

class ListImportacao(BaseModel):
    importacao:list[Importacao]

class Exportacao(BaseModel): 
    paises: str
    quantidade: int | None
    valor: int | None

class ListExportacao(BaseModel):
    exportacao:list[Exportacao]