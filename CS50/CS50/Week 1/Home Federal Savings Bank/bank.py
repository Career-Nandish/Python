import re
greet = input("Greeting: ").strip().lower()
if re.match(r'^hello.*$', greet):
    print("$0")
elif greet[0] == 'h':
    print("$20")
else:
    print("$100")