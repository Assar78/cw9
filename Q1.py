import re

def valid_pass(password):

    """
    the pass should have one digit,
    one capital letter,
    one small letter 
    to be validated.
    """

    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    result = re.match(pattern, password) 
    return result

password = input("Enter password: ")
print(valid_pass(password))