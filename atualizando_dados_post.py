from conexao_post import conn


cursor_obj = conn.cursor()


# Criando a variável SQL
sql = """
    UPDATE game
    SET name = %s
    WHERE id = %s
"""

cursor_obj.execute(sql, ("Fifa 23", 5))
conn.commit()
print("Dados atualizados com sucesso!")
conn.close()