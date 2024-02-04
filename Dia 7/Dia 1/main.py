from MODULOS import suma
from MODULOS import obtener_numero
from MODULOS import saludar

# ------ Funciones ------
# 1. Función con parámetros y con retorno
def suma(a, b):
    resultado = a + b
    return resultado

# Uso de la función
valor1 = 5
valor2 = 3
resultado_suma = suma(valor1, valor2)

print(f"La suma de {valor1} y {valor2} es: {resultado_suma}")

# 2. Función sin parámetros y con retorno
def obtener_numero():
    return 42

# Uso de la función
resultado = obtener_numero()

print(f"El número obtenido es: {resultado}")

# 3. Función con parámetros y sin retorno
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Uso de la función
nombre_usuario = "Daniel"
saludar(nombre_usuario)


# 4. Función sin parámetros y sin retorno
def saludar():
    print("¡Hola, mundo!")

# Uso de la función
saludar()



