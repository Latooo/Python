import json

#Separe por partes el archivo json para poder manipularlo
ejercicio1 = open("data.json")
ejercicio = json.load(ejercicio1)
print("CLIENTES\n")
clientes = ejercicio["ventas"]["clientes"]
print(clientes)
print(type(clientes))
print("COMERCIALES\n")
comerciales = ejercicio["ventas"]["comerciales"]
print(comerciales)
print(type(ejercicio))
print("PEDIDOS\n")
pedidos = ejercicio["ventas"]["pedidos"]
print(pedidos)
print(type(ejercicio))

#Ejercicio 1

pedidos_ordenados = sorted(pedidos, key=lambda x: x["fecha"], reverse=True)
print(pedidos_ordenados)

datatxt = json.dumps(pedidos_ordenados)
with open('data.json','w') as outfile:
   outfile.write(datatxt)
    