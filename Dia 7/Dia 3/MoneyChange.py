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