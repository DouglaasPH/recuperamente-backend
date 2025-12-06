import sqlite3

from fastapi import APIRouter

from models import dados_pera_registrar_conta, dados_para_conectar, verificar_login, dados_para_adicionar_nota


router = APIRouter(
    prefix=""
)


#aqui é a estrutura da conexão com o banco de dados
def pegar_conexao_db():
    conexao = sqlite3.connect("banco_de_dados.db")
    conexao.row_factory = sqlite3.Row
    return conexao


# RESPONSÁVEL = DOUGLAS
#aqui é feita a rota 
@router.post("/cadastrar")
#aqui é feita a definição da função + a linkagem com o modelo de dados que vai ser enviado
def realizar_login(dados_para_registar_conta: dados_pera_registrar_conta): #JALDSON ALTEROU O NOME DA FUNÇÃO PRA EVITAR ERROS
    conexao = pegar_conexao_db()
    conexao.execute(
    "INSERT INTO usuarios (nome, email, senha) VALUES (?,?,?)",
    (dados_para_registar_conta.nome, dados_para_registar_conta.email, dados_para_registar_conta.senha)
    
    )
    #aqui o commit serve pra salvar o arquivo
    conexao.commit()
    #aqui o close serve pra fechar
    #em geral essa estrutura serve pra salvar, e fechar,
    #o arquivo de forma segura
    conexao.close()
    return ("Resposta: Operação Realizada Com Sucesso!")


# RESPONSÁVEL = JALDSON
#aqui é feita a rota 
@router.post("/conectar")
#aqui é feita a definição da função + a linkagem com o modelo de dados que vai ser enviado
def conectar(conectar: dados_para_conectar): #JALDSON ALTEROU O NOME DA FUNÇÃO PRA EVITAR ERROS
    #aqui é feita a linkagem com o banco de dados
    conexao = pegar_conexao_db()
    #aqui é criada a variável execucao pra rodar os comandos das pesquisa
    execucao = conexao.execute(
    "SELECT usuarios.id FROM usuarios WHERE email =? AND senha =?", #ANALISAR DEPOIS
    #aqui é onde é feita a requisição dos dados pra executar os comandos
    (conectar.email, conectar.senha)
    
    )
    #aqui o fetch "guarda" os dados que ele encontrou e guarda na variável verificacao
    usuario = execucao.fetchall()
    conexao.close()
    
    #aqui é aplicada uma verificação condicional pra retornar uma mensagem  
    #para o comando enviado
    if usuario:
        return {"Resposta": "Login Realizado Com Sucesso", "usuario_id": usuario.id}
    else:
        return {"Resposta": "Login Não Realizado ---> Credenciais Incorretas"}
    

# RESPONSÁVEL = JALDSON
#aqui é feita a rota 
@router.post("/verificar_login")
#aqui é feita a definição da função + a linkagem com o "modelo de dados" que vai ser enviado
def verificar_login(login: verificar_login):
    #aqui é feita a linkagem com o banco de dados
    conexao = pegar_conexao_db()
    #aqui é criada a variável execucao pra rodar os comandos das pesquisas
    execucao = conexao.execute(
    "SELECT id FROM usuarios WHERE id=?",
    #aqui é onde se "insere o modelo" de dados que vai ser enviado
    (login.id_usuarios,)
    
    )
    #aqui o fetch "guarda" os dados que ele encontrou e guarda na variável verificacao
    verificacao = execucao.fetchall()
    conexao.close()
    
    #aqui é aplicada uma verificação condicional pra retornar uma mensagem caso o usuário 
    #esteja logado ou não
    if verificacao:
        return {"Resposta": "Verificação Realizado Com Sucesso", "usuarios_id": verificacao}
    else:
        return {"Resposta": "A Verificação Não Encontrou O Usuário ---> Credenciais Incorretas", "usuarios_id": verificacao}

# RESPONSÁVEL: TEIXEIRA
@router.post("/adicionar-nota")
def adicionar_nota(dados: dados_para_adicionar_nota):
    #aqui é feita a linkagem com o banco de dados
    conexao = pegar_conexao_db()

    #aqui é criada a variável execucao pra rodar os comandos das pesquisas
    execucao_usuario = conexao.execute(
        "SELECT id FROM usuarios WHERE id=?",
        (dados.id_usuario,)
    )
    usuario_existente = execucao_usuario.fetchall()

    #caso usuário não exista
    if not usuario_existente:
        conexao.close()
        return {"Resposta": "Erro: Usuário não encontrado", "status": "falha"}

    # 3) Inserir a nota no banco
    conexao.execute(
        "INSERT INTO calendario (usuario_id, data, descricao_da_data) VALUES (?, ?, ?)",
        (dados.id_usuario, dados.data, dados.conteudo)
    )

    # 4) Salvar e fechar
    conexao.commit()
    conexao.close()

    # 5) Resposta de sucesso
    return {"Resposta": "Nota adicionada com sucesso!", "status": "sucesso"}

# RESPONSÁVEL: TEIXEIRA
#aqui é feita a rota 
@router.get("/notas")
def listar_notas(id_usuario: int):
    #aqui é feita a linkagem com o banco de dados
    conexao = pegar_conexao_db()

    # Buscar notas no banco
    execucao = conexao.execute(
        "SELECT id, data, descricao_da_data FROM calendario WHERE usuario_id=?",
        (id_usuario,)
    )

    # Salva as notas e fechar
    notas = execucao.fetchall()
    conexao.close()

    # Transformar os resultados em lista de dicionários
    lista_notas = [
        {
            "id": nota["id"],
            "data": nota["data"],
            "conteudo": nota["conteudo"]
        }
        for nota in notas
    ]

    return {
        "id_usuario": id_usuario,
        "total_notas": len(lista_notas),
        "notas": lista_notas
    }
