import sqlite3

connection = sqlite3.connect('title.db')


cursor = connection.cursor()

# Solicitando dados do usuário
# Ao atulizar os dados é necessario definir uma condição, essa condição geralmente é chamada de cláusula where
id = int(input("Informe o id do filme que deseja atualizar: \n"))
name = input("Digite o nome do filme: \n")

# Atualizando os dados
cursor.execute("""
        UPDATE movies set name = ?
        WHERE id = ?

""", (name, id))
connection.commit()
print("Dados atualizados com sucesso")


connection.close()