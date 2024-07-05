def main():
    in_str = input("Input: ")
    print("Output:", remove_vowels(in_str))

def remove_vowels(s):
    out_str = ''
    for i in s:
        if not i.lower() in 'aeiou':
            out_str += i
    return out_str

if __name__ == "__main__":
    main()