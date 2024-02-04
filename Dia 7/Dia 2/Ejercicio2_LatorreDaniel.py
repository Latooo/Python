from MODULOS import BienvenidaMensaje

import random

def BienvenidaMensaje():
    print("Adivina el numero!")
    print("Intenta adivinar el número secreto entre 1 y 100. Tienes 10 intentos.")
    
    # Generar un número secreto aleatorio
    numeroSecreto = random.randint(1, 100)
    intentos = 0

    while intentos < 10:
        try:
            adivina = int(input("Ingresa tu numero: "))

            if adivina < 1 or adivina > 100:
                print("Ingresa un número entre 1 y 100.")
                continue

            intentos += 1

            if adivina == numeroSecreto:
                print(f"Adivinaste el número secreto {numeroSecreto} en {intentos} intentos.")
                break
            elif adivina < numeroSecreto:
                print("El número secreto es mayor. Intenta nuevamente.")
            else:
                print("El número secreto es menor. Intenta nuevamente.")

        except ValueError:
            print("Error: Ingresa un número válido.")

    if intentos == 10:
        print(f"Se acabaron tus 10 intentos. El número secreto era {numeroSecreto}.")


BienvenidaMensaje()