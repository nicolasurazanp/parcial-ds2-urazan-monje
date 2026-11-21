from pymongo import MongoClient

URI = "mongodb://localhost:27017/"

URI = "mongodb://admin:123456@localhost:27017/?authSource=admin"

client = MongoClient(URI)

db = client["MatriculApp"]

tickets_col = db["tickets"]
semanas_col = db["semanas"]
agentes_col = db["agentes"]


