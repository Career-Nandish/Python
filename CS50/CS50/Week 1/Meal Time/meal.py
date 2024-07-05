def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    print(tell_meal(converted_time))

def tell_meal(t):
    if 7.00 <= t <= 8.00:
        return "breakfast time"
    elif 12.00 <= t <= 13.00:
        return "lunch time"
    elif 18.00 <= t <= 19.00:
        return "dinner time"
    else:return None


def convert(time):
    hour, minutes = [int(i) for i in time.split(":")]
    return round(hour + minutes/60, 2)


if __name__ == "__main__":
    main()
