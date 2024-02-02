## DIA 1

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

##DIA 2
##Ejercicio 1
def fibonacci(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

def BienvenidaMensaje():
    print("¡Bienvenido al Generador de la Secuencia de Fibonacci!")
    print("Ingresa un número entero para generar la secuencia hasta ese término.")
    print("Si deseas salir, ingresa 0.")

def main():
    BienvenidaMensaje()
##Ejercicio 2
def BienvenidaMensaje():
    print("Adivina el numero!")
    print("Intenta adivinar el número secreto entre 1 y 100. Tienes 10 intentos.")

##DIA 3
##MoneyChange

def change(quantity):
    coin10 = quantity // 10
    quantity %= 10
    coin5 = quantity // 5
    quantity %= 5
    coin1 = quantity

    return coin10, coin5, coin1

def cashier():
    while True:
        try:
            quantity = int(input("Enter the money: "))
            if quantity <= 0:
                print("Not valid")
            else:
                break
        except ValueError:
            print("Not valid")

    coin10, coin5, coin1 = change(quantity)

    print(f"\nDeliver \n{coin10} coins of 10\n{coin5} coins of 5\n{coin1} coins of 1.")    

##DIA 4
def count_pairs(k, numbers):
    count = 0
    remainder_count = [0] * k

    for num in (numbers):
        remainder = num % k
        complement = (k - remainder) % k
        count += remainder_count[complement]
        remainder_count[remainder] += 1

    return count

##DIA 5
##DIA 6
import math
def Colision(bola1, bola2):
    x1, y1, r1 = bola1
    x2, y2, r2 = bola2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance <= r1 + r2

bola1 = (0,0,5)
bola2 = (8,0,3)

print(Colision(bola1, bola2))

def Colision(bola1, bola2):
    x1, y1, z1, r1 = bola1
    x2, y2, z2, r2 = bola2
    distance_euclides = math.sqrt((x2 - x1)**2 + (y2 - y1)) + (z2 - z1)**2
    print(distance_euclides)
    return distance_euclides <= r1 + r2