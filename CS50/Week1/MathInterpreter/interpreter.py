expr = input("Expression: ").strip()
x, y, z = expr.split(" ")
x = int(x)
z = int(z)
match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))