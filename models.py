# Importa o BaseModel da biblioteca Pydantic.
# O BaseModel permite criar modelos de dados com validação automática.
from pydantic import BaseModel


# RESPONSÁVEL: DOUGLAS
# Modelo de dados usado quando alguém quer registrar uma nova conta.
# Ele define quais informações são obrigatórias e de qual tipo.
class dados_pera_registrar_conta(BaseModel):
    nome: str   # O nome do usuário (texto)
    email: str  # O email do usuário (texto)
    senha: str  # A senha que o usuário escolhe (texto)


# RESPONSÁVEL: JALDSON
# Modelo de dados usado quando alguém quer fazer login/conectar na conta.
# Aqui só é necessário email e senha.
class dados_para_conectar(BaseModel):
    email: str  # O email usado no login (texto)
    senha: str  # A senha usada no login (texto)


# RESPONSÁVEL: JALDSON
# Modelo usado para verificar se um login foi bem-sucedido.
# Ele contém o ID do usuário após a autenticação.
class verificar_login(BaseModel):
    id_usuarios: int  # O identificador numérico do usuário (número inteiro)

# RESPONSÁVEL: TEIXEIRA
class dados_para_adicionar_nota(BaseModel):
    id_usuario: int
    data: str
    conteudo: str