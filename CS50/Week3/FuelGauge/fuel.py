class FormatError(Exception):
    def __init__(self, message = None):
        self.message = message
        super().__init__(message)

def get_tank_read(prompt):
    while True:
        try:
            inp = input(prompt)
            if '/' in inp:
                x, y = [int(i) for i in inp.split("/")]
                if x > y and y !=0 :raise ValueError
                else:return round(x*100/y)
            else:
                raise FormatError
        except FormatError:
            print("Format of the input must be x/y")
        except ValueError:
            print("x and y must be integers where x<=y")
        except ZeroDivisionError:
            print("y can not be 0")

def read_indicator(ind):
    if ind <= 1:
        return "E"
    elif  1 < ind < 99:
        return str(ind) + "%"
    else:
        return "F"

def main():
    indicator = get_tank_read("Enter the value of x and y(format: x/y):")
    print(read_indicator(indicator))

if __name__ == "__main__":
    main()