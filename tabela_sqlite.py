import sqlite3

#  1 - Criando no DB
connection = sqlite3.connect('title.db')
print(connection)
# Para criar a tabela precisa do cursor, 
# esse cursor não é nada mais que um operador que permite
# navegar e manipular os dados
#   Operação DDL - operação de manipulação de estrutura de dados
#   Operação DML - operação de manipulação de dados


#  2 - Criando cursor
cursor = connection.cursor()

# 3 - Criar a tabela
cursor.execute("""
    CREATE TABLE movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
               
    );
               """)


# 4 - Fechando conexão 
print("Tabela criada com sucesso")
connection.close()
