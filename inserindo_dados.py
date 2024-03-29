import sqlite3

connection = sqlite3.connect('title.db')

cursor = connection.cursor()

# Inserindo os dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Super Mario Bros', '2023', '10')
""")

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Velozes e Furiosos 10', '2023', '8')
""")


cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Avatar', '2023', '10')
""")

# Gravando dados no BD
connection.commit()
print("Dados inserindos com sucesso")

# Gravando dados
connection.close()
