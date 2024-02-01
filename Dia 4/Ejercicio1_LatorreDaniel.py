import math

def count_pairs(k, numbers):
    count = 0
    remainder_count = [0] * k

    for num in (numbers):
        remainder = num % k
        complement = (k - remainder) % k
        count += remainder_count[complement]
        remainder_count[remainder] += 1

    return count

T = int(input("CASOS: "))

for case_num in range(1, T+1):
    nk = input(f"n y k de caso #{case_num} ").split()
    n, k = map(int, nk[:2])

    numbers = list(map(int, input(f"Ingrese {n} números separados por espacio: ").split()))
    print(numbers)

    result = count_pairs(k, numbers)
    print(result)
    print(f"Case {case_num}: {result}")