from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

myquery = {"category": "Data analysis"}

x = mycol.delete_one(myquery)

print(f"{x.deleted_count} documento excluído")