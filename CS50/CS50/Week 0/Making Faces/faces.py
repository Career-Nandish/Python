def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁')

def main():
    text = input("Write your text here : ")
    print(convert(text))

if __name__ == "__main__":
    main()