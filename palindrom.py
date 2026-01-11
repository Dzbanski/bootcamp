
def is_palindrom(name):
    """
    Function is_Palindrom take string and lower his letters
    Return True or False if string is equal with reversed string
    """
    name_low = name.lower()
    
    return name_low == name_low[::-1]

check_palindrom = is_palindrom("Kajak")

print(check_palindrom)

