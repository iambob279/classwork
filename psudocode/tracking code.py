code = input("Please input your tracking code = ").lower()

def check(code):
    length = len(code)
    start = code[0]
    if length > 8:
        return ("Invalid")
    if start == "p" or "q":
        return ("valid")
    return ("invalid")

print(check(code))