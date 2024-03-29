import sqlite3

connection = sqlite3.connect('title.db')

cursor = connection.cursor()

# Solicitando dados do usuário

name = input("Digite o nome do filme: \n")
year = int(input("Digite o ano do filme: \n"))
score = float(input("Digite a nota do filme: \n"))

# Inserindo dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)
""", (name, year, score))

# Ao inves de passar valores de forma direta,
# eles são passados como parametro

# Gravando dados no BD
connection.commit()
print("Dados inserindos com sucesso")

# Gravando dados
connection.close()
