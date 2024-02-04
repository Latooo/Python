from MODULOS import count_pairs

T = int(input("CASOS: "))

for case_num in range(1, T+1):
    nk = input(f"n y k de caso #{case_num} ").split()
    n, k = map(int, nk[:2])

    numbers = list(map(int, input(f"Ingrese {n} números separados por espacio: ").split()))
    print(numbers)

    result = count_pairs(k, numbers)
    print(result)
    print(f"Case {case_num}: {result}")
