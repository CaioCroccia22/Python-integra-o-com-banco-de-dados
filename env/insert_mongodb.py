from pymongo import MongoClient

# Estabelecendo conexão
client = MongoClient()

# Criando\Acessando o database
mydb = client.obcblog

# Acessando a collection
mycol = mydb.posts


post1 = {
    "title": "Streamlit",
    "category": "Data analysis",
    "author": {
        "name": "Teste",
        "email": "teste@gmail.com"
    }
    
}

result = mycol.insert_one(post1)
print("Dado incluido com sucesso!!!")