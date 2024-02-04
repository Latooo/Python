
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

