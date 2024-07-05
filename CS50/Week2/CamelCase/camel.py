def camelToSnakeCase(s):
    snake_string = ''
    for i in s:
        if not i.isupper():
            snake_string += i
        else:
            snake_string += ('_' + i.lower())
    return snake_string

def main():
    camel_string = input("camelCase: ")
    print('snake_case:', camelToSnakeCase(camel_string))

if __name__ == "__main__":
    main()