import json

crudbase = open("crud.json")
crud = json.load(crudbase)

#CRUD clientes
print("CLIENTES\n")
clientes = crud["ventas"]["clientes"]
print(clientes)
print(type(clientes))

#CRUD comerciales
print("COMERCIALES\n")
comerciales = crud["ventas"]["comerciales"]
print(comerciales)
print(type(crud))
print("PEDIDOS\n")

#CRUD pedidos
pedidos = crud["ventas"]["pedidos"]
print(pedidos)
print(type(crud))




    