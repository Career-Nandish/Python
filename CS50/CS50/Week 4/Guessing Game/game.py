import random

def get_input(prompt):
    while True:
        try:
            inp = int(input(prompt))
            if inp > 0:
                break
        except ValueError:
            pass
    return inp

def check_guess(inp):
    while True:
        guess = get_input("Guess: ")
        if guess < inp:
            print("Too small!")
        elif guess > inp:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

def main():
    inp = get_input("Level: ")
    check_guess(random.randint(1,inp))

if __name__ == "__main__":
    main()