import json


ejercicio1 = open("data.json")
ejercicio = json.load(ejercicio1)
print("PEDIDOS\n")
print(ejercicio["ventas"]["pedidos"])
print(type(ejercicio))