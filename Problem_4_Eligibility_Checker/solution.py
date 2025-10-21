age = int(input("Enter your age: "))
has_license = input("Do you have a valid driver's license? (yes/no): ").strip().lower()

if age >= 18 and has_license == "yes":
    print("You are eligible for the role.")
else:
    print("You are not eligible for the role.")
