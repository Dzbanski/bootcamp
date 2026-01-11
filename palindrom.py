
def is_palindrom(name):
    name_low = name.lower()
    
    return name_low == name_low[::-1]

check_palindrom = is_palindrom("Kajak")

print(check_palindrom)

