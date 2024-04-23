import requests
from pymongo import MongoClient


# 1 - Estabelece conexão com o MongoDB
client = MongoClient()


# 2 - Criando o database
db = client['nobel']

# 3 - Importar dados em Documentos
for collection_name in ["prizes", "laureates"]:
    response = requests.get(
        # Requisição da API
        f"http://api.nobelprize.org/v1/{collection_name[:-1]}.json")
        
    documents = response.json()[collection_name]
    db[collection_name].insert_many(documents)
    
    

# 4 - Acessando coleções / Contagem de documentos na coleção
prizes = db["prizes"]
laureates = db["laureates"]

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})


print(len_prizes)
print(len_laureates)