import re
import sys

# def validate(ip):
#     pattern = re.compile(r"""
#         ^
#             (
#                 (25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.
#             ){3}
#             (25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])
#         $
#         """, re.X)
#     if pattern.match(ip):
#         return True
#     return False

def validate(ip):
    try:
        if matches:= re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
            return all([0<=int(i)<=255 for i in matches.groups()])
        return False
    except:
        return False

def main():
    print(validate2(input("IPv4 Address: ").strip()))

if __name__ == "__main__":
    main()