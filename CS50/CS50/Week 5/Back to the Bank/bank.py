import re

def main():
    greet = input("Greeting: ")
    print(value(greet))


def value(greet):
    greet  = greet.lower().lstrip()
    if re.match(r'^hello.*$', greet): return 0
    elif greet[0] == 'h': return 20
    else: return 100

if __name__ == "__main__":
    main()