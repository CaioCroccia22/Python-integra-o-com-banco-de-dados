import sqlite3

connection = sqlite3.connect("title.db")


cursor = connection.cursor()

#  Lendo os dados da tabela
data = cursor.execute("""
    SELECT name, year, score FROM movies
                      
            """)
            
print(data.fetchall())

# Iterando os dados 
for row in cursor.execute("SELECT * FROM movies ORDER BY id"):
    print(f"{row}")


connection.close()
        

