# RESPONSÁVEL = ARTHUR
# Importa a classe FastAPI, que permite criar a aplicação web
from fastapi import FastAPI

# Importa o middleware de CORS, que controla quais sites podem acessar sua API e fazer requisições
from fastapi.middleware.cors import CORSMiddleware

# Importa o rotas definidas em "routes.py"
from routes import router

# Cria a aplicação FastAPI
app = FastAPI()

# Adiciona as rotas do arquivo "routes" à aplicação
app.include_router(router)

# Adiciona o middleware de CORS para permitir que outros sites/acessos chamem a API
app.add_middleware(
    CORSMiddleware,

    # O "*" indica que não há restrição de origem.
    # allow_origins=["*"] significa que qualquer site pode acessar a API
    allow_origins=["*"],
    
    # allow_methods=["*"] permite que qualquer método HTTP seja usado (GET, POST, PUT e DELETE)
    allow_methods=["*"],
    
    # allow_headers=["*"] permite que a API aceite qualquer cabeçalho enviado nas requisições
    allow_headers=["*"],
)
