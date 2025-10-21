# your code here
name = input("What is your name? ")
food = input("What is your favorite food? ")
current_year = int(input("What year is it currently? "))
age = int(input("How old are you? "))

birth_year = current_year - age

print(f"Hello, {name}! It's great to know you love {food}.")
print(f"You are {age} years old, so you were likely born in {birth_year}.")
