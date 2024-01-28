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

    while True:
        try:
            n = int(input("Ingrese el término hasta el cual desea generar la secuencia (ingrese 0 para salir): "))
            
            if n < 0:
                print("Por favor, ingresa un valor entero no negativo.")
                continue
            
            if n == 0:
                print("¡Gracias por usar el Generador de Fibonacci!")
                break
            
            secuencia = fibonacci(n)
            print(f"Secuencia de Fibonacci hasta el término {n}: {secuencia}")

        except ValueError:
            print("Error: Por favor, ingresa un valor entero válido.")
            continue

if __name__ == "__main__":
    main()
