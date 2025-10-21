import re

password = input("Enter your password: ")

length_ok = len(password) >= 8
has_upper = re.search(r'[A-Z]', password)
has_lower = re.search(r'[a-z]', password)
has_digit = re.search(r'\d', password)
has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

if length_ok and has_upper and has_lower and has_digit and has_special:
    print("Password is strong.")
else:
    print("Password is weak.")
