import sqlite3

connection = sqlite3.connect('title.db')

# Solicitando os dados para o usuário para excluir
id = int(input("Escolha o filme para remover da tabela: \n"))
cursor = connection.cursor()
cursor.execute("""
            DELETE FROM movies
            WHERE id = ?
""", (id,))

connection.commit()

print("Filme deletado com sucesso!!")

connection.close()