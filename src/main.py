from pymongo import MongoClient
from CampanaPruebas import CampanaPruebas 


client = MongoClient("mongodb://admin:123456@localhost:27017/?authSource=admin")
db = client["MatriculApp"]
coleccion = db["semanas"]

datos_mongo = list(coleccion.find().sort("semana", 1))

campana = CampanaPruebas(datos_mongo)
a, b = campana.ajustar()


print(f"Parametros encontrados --> a = {a:.2f}, b = {b:.4f}")
print(f"1. Defectos que quedan sin descubrir si se suelta hoy: {campana.restantes():.2f}")
print(f"2. semana en la que se llega al 95%: {campana.semana_95():.2f}")

campana.graficar()
print("la grafica se guardo en la carpeta graficas")







