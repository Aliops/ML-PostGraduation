from fastapi import FastAPI, Path, HTTPException, status, Depends
from datetime import date
from typing import Annotated
import datacess 
from entities import Producao, ListProducao, Processamento, ListProcessamento, Comercializacao, ListComercializao, Importacao, ListImportacao, Exportacao, ListExportacao
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from entities import Base, User 
from models import User as UserModel, Token
from auth import create_access_token, decode_access_token
from utils import get_password_hash, verify_password

app = FastAPI()

Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = decode_access_token(token)
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(User).filter(User.username == token_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@app.get("/users/me", response_model=UserModel)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/users/", response_model=UserModel)
def create_user(user: UserModel, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
   
def validation_year(year: Annotated[int, Path(examples = 1970)]):
    if year not in range (1970, date.today().year): 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "year not valid") #criando uma exception universal para validation_year
    return year

#def validation_subopt(subopt: Annotated[int, Path(ge=1,)]):
#    if subopt not in range(1, )

@app.get('/producao/{year}', response_model= ListProducao)  # response model tem que ser modelo do pydentic - pesquisar o que pydentic
def get_producao(year: Annotated[int, Depends(validation_year)]): #força para que seja int
   producoes_data = datacess.producao(year)
   producoes = [Producao(produto = row ['Produto'], quantidade = row['Quantidade (L.)']) for _,row in producoes_data.fillna('').replace({'Quantidade (L.)': r'^(.*\D.*|)$'}, {'Quantidade (L.)' : None}, regex = True).iterrows()]
   return ListProducao(producoes=producoes)
    #OK
#cmo utilizar o pydentic - otimizar o códigoo
   
   
@app.get('/processamento/{year}/{subopt}', response_model= ListProcessamento)
def get_processamento(year: Annotated[int, Depends(validation_year)], subopt: Annotated[int, Path(ge=1, le=4)]):
    processamento_data = datacess.processamento(year,subopt) 
    processamento = [Processamento(cultivar = row ['Cultivar'], quantidade = row ['Quantidade (Kg)'], sclaissificacao= row ['Sem definição']) for _,row in processamento_data.fillna('').replace({'Quantidade (Kg)': r'^(.*\D.*|)$'}, {'Quantidade (Kg)' : None}, regex = True).iterrows()]
    return ListProcessamento(processamento=processamento)
   #ta falando que na coluna 'sem classificacao' não tem cultivar, como fazer pra pegar só o cultivar das colunas que tem cultivar
    
@app.get('/comercializacao/{year}', response_model= ListComercializao)  
def get_comercializacao(year: Annotated[int, Depends(validation_year)]):
    comercializacao_data = datacess.comercializacao(year)
    comercializacao= [Comercializacao(produto=row['Produto'],quantidade=row['Quantidade (L.)']) for _,row in comercializacao_data.fillna('').replace({'Quantidade (L.)': r'^(.*\D.*|)$'}, {'Quantidade (L.)' : None}, regex = True).iterrows()]
    return ListComercializao(comercializacao=comercializacao)
    #OK

@app.get('/importacao/{year}/{subopt}',response_model= ListImportacao)  
def get_importacao(year:Annotated[int, Depends(validation_year)], subopt: Annotated[int, Path(ge=1, le=5)]):
    importacao_data = datacess.importacao(year,subopt)
    importacao= [Importacao(paises = row ['Países'], quantidade = row['Quantidade (Kg)'], valor = row['Valor (US$)']) for _,row in importacao_data.fillna('').replace({'Quantidade (Kg)': r'^(.*\D.*|)$', 'Valor (US$)': r'^(.*\D.*|)$'}, {'Quantidade (Kg)' : None, 'Valor (US$)': None}, regex = True).iterrows()]
    return ListImportacao(importacao=importacao)
    #falando que o numero tem que ser finito

@app.get('/exportacao/{year}/{subopt}', response_model= ListExportacao)  
def get_exportacao(year: Annotated[int, Depends(validation_year)], subopt: Annotated[int, Path(ge=1, le=4)]):
    exportacao_data= datacess.exportacao(year,subopt)
    exportacao= [Exportacao(paises=row['Países'], quantidade=row['Quantidade (Kg)'], valor=row['Valor (US$)']) for _,row in exportacao_data.fillna('').replace({'Quantidade (Kg)': r'^(.*\D.*|)$', 'Valor (US$)': r'^(.*\D.*|)$'}, {'Quantidade (Kg)' : None, 'Valor (US$)': None}, regex = True).iterrows()]
    return ListExportacao(exportacao=exportacao)
     #falando que o numero tem que ser finito


