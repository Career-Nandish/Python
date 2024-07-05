def take_grocery_list():
    grocery_dict = {}
    while True:
        try:
            item = input().upper()
            if item not in grocery_dict:
                grocery_dict[item] = 1
            else:
                grocery_dict[item] += 1
        except EOFError:
            return grocery_dict

def prettify_grocery_list(d):
    grocery_list = ''
    for k in sorted(d.keys()):
        grocery_list += (str(d[k]) + ' ' +  k)
        grocery_list += '\n'
    return grocery_list

def main():
    print(prettify_grocery_list(take_grocery_list()))

if __name__ == "__main__":
    main()