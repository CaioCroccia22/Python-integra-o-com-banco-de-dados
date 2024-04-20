from pymongo import MongoClient

# Estabelecendo conexão
client = MongoClient()

# Criando o database
mydb = client.obcblog

# Criando a collection
mycol = mydb.posts


post1 = {
    "title": "WebScraping",
    "category": "Automação",
    "author": {
        "name": "Caio Croccia",
        "email": "caio.croccia@gmail.com"
    }
    
}

result = mycol.insert_one(post1)
print("Dado incluido com sucesso!!!")