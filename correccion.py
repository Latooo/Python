def calcular_definitiva(lista):
    lista[0]=lista[0]*0.3
    lista[1]=lista[1]*0.3
    lista[2]=lista[2]*0.4
    sumatoria=0
    for i in range(len(lista)):
        sumatoria=sumatoria+lista[i]

    return sumatoria


for i in range(5):
    print("Estudiante#",i+1)
    lista=[]
    notaMayor=0
    definitiva=0
    for i in range(3):
        if(i==2):
            numerito=(float(input("Ingresa tu nota:")))
            print(numerito)
            definitiva=definitiva+numerito
            if(numerito>notaMayor):
                notaMayor=numerito
            lista.append(numerito)
        else:
            numerito=(float(input("Ingresa tu nota:")))
            print(numerito)
            definitiva=definitiva+numerito
            if(numerito>notaMayor):
                notaMayor=numerito
            lista.append(numerito)
    print(lista)

    if(lista.index(notaMayor)==2):
        print("Tu nota mayor es:",(notaMayor))
    else:
        print("Tu nota mayor es:",(notaMayor))

    definitiva=calcular_definitiva(lista)
    print("Tu definitiva es:",definitiva)

    if(definitiva<2):
        print("Perdiste tu vida.")
    elif (definitiva<3):
        print("Pues... todo bien...recupera")
    elif(definitiva>4.5):
        print("Excelente estudiante! Sos ejemplar")
    elif(definitiva>=3):
        print("Aprobaste pero aun puedes mejorar")