from conexao_post import conn

cursor_obj = conn.cursor()

sql = """
    DELETE FROM game
    WHERE id = %s
    
"""

# sumary_line
# Keyword arguments
# argument -- description
# Return: return_description

cursor_obj.execute(sql, (6,))
# Coloca virgula depois do 6 para enteder que é um tupla e não uma string

conn.commit()

print("Dados excluidos com sucesso!")