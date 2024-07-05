def main():
    m = int(input("Enter the value of m(in kg) = "))
    c = 300000000  # meters per second
    
    e = m * (c ** 2)
    print(f"E = {e}")

if __name__ == "__main__":
    main()