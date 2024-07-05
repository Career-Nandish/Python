def take_order(prompt, menu):
    total = 0
    while True:
        try:
            item = input(prompt).title()
            if item not in menu:
                print(f"We don't sell {item}s")
            else:
                total += menu[item]
                print(f"Total: ${total:.2f} ")
        except EOFError:
            print(f"\nThanks for your order, your total is ${total:.2f}.")
            break

def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    take_order("What would you like to have?: ", menu)

if __name__ == "__main__":
    main()