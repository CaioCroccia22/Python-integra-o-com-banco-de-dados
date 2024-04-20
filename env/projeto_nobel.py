import requests
from pymongo import MongoClient


# 1 - Estabelece conexão com o MongoDB
client = MongoClient()

db = client['nobel']