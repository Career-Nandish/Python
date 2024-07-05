def main():
    balance = 50
    accepted_denom = [25, 10, 5]
    while balance > 0:
        print("Amount Due:", balance)
        insert = int(input("Insert Coin: "))
        if insert in accepted_denom:
            if balance > insert:
                balance -= insert
            else:
                print("Change Owed:", insert - balance)
                break
        else:
            pass

if __name__ == "__main__":
    main()