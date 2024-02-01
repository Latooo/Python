#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO

diccionario = {"Productos": ("Papas", "Gaseosas", "Jugos"),
               "Precios": (3000, 6000, 4000)}
print("Lista de productos")
print(diccionario)

producto = str (input("Ingrese el producto que desea de la lista anterior: "))
cantidad = int (input("Ingrese la cantidad que desea de este producto: "))
producto = producto.capitalize()
precioTotal = int


if producto in diccionario["Productos"] :
    precioTotal = diccionario["Precios"][0]
    precioTotal = precioTotal * cantidad

print(precioTotal)

    