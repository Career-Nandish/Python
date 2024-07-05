def main():
    in_str = input("Input: ")
    print("Output:", shorten(in_str))

def shorten(s):
    if s.isdigit():
        return s
    else:
        out_str = ''
        for i in s:
            if (i not in 'aeiou') or i.isdigit():
                out_str += i
        return out_str

if __name__ == "__main__":
    main()