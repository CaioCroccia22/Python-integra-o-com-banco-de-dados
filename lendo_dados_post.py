from conexao_post import conn

# Criando o cursor
cursor_obj = conn.cursor()

# Realizando a query
cursor_obj.execute("SELECT *  FROM GAME")

# Listar todos os registros
result = cursor_obj.fetchall()

# Printar os resultados
print(result)