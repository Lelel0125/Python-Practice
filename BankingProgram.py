# Python Banking Program

def showBalance(balance):
    print("****************************")
    print(f"Your balance is ${balance:.2f}")
    print("****************************")

def Deposit():
    print("****************************")
    depo = float(input("Enter an amount to be deposited: "))
    print("****************************")

    if depo < 0:
        return 0
    else:
        return depo

def Withdraw(balance):
    print("****************************")
    withd = float(input("Enter an amount to be withdrawn: "))
    print("****************************")

    if withd > balance:
        print("Insufficient funds")
        return 0
    elif withd < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return withd


def main():
    balance = 0
    is_running = True


    while is_running:
        print("****************************")
        print("       Banking Program      ")
        print("****************************")

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        print("****************************")

        choice = int(input("Enter your choice (1-4): "))

        match  choice:
            case 1:
                showBalance(balance)
            case 2:
                balance += Deposit()
            case 3:
                balance -= Withdraw(balance)
            case 4:
                is_running = False
            case _:
                print("That is not a valid choice")

    print("Thank you! have a nice day!")

if __name__ == '__main__':
    main()