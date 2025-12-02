import sqlite3

# 1. Conecta ao banco (cria o arquivo se não existir)
conector = sqlite3.connect("banco_de_dados.db")


# 2. Cria um executor para executar comandos SQL
executor = conector.cursor()


# 3. Cria uma tabela (se não existir)
executor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")


# 3. Cria uma tabela (se não existir)
executor.execute("""
CREATE TABLE IF NOT EXISTS calendario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INT NOT NULL,
    data date NOT NULL,
    descricao_da_data TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")

#RESPONSÁVEL: TEIXEIRA
# 3. Cria uma tabela (se não existir)
executor.execute("""
CREATE TABLE IF NOT EXISTS notas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    data date NOT NULL,
    conteudo TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")

# 4. Salva as alterações e fecha a conexão
conector.commit()
conector.close()


print("Banco de dados inicializado com sucesso!")


