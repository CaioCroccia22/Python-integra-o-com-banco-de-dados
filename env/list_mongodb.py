from pymongo import MongoClient
from pprint import pprint

# pprint ajuda a formatar melhor os dados

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

# Retorna um documento
# result = mycol.find_one()

# Retorna todos os documentos
result = mycol.find()


for r in result: 
    pprint(r)
    # Como ele retorna um cursor, tem que interar o objeto de cursor
print(result)