from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('God of war 4', 2022, 10),
    ('Star Wars', 2023, 9.8)
]

for game in games:
    cursor_obj.execute("""

        INSERT INTO game(name,year, score)
        VALUES (%s, %s, %s)
""", game)

conn.commit()

print("Dados atualizados com sucesso!!")

conn.close()