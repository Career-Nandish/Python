import random

def main():
    level = get_level()
    problems = generate_problems(level)
    score = run_quiz(problems)
    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    """Generate a random non-negative integer with the specified number of digits."""
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

def generate_problems(level):
    problems = []
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problems.append((x, y, x + y))
    return problems

def run_quiz(problems):
    score = 0
    for x, y, answer in problems:
        attempts = 0
        while attempts < 3:
            try:
                response = int(input(f"{x} + {y} = "))
                if response == answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            attempts += 1
        if attempts == 3:
            print(f"{x} + {y} = {answer}")
    return score

if __name__ == "__main__":
    main()