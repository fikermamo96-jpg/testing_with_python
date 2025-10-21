"""
Input an intiger and num ber of shift positions.
number = int(input("Enter an integer: "))
shifts = int(input("Enter number of shift positions: "))

Show results of left shift and right shift.
left_shift = number << shifts
right_shift = number >> shifts

print(f"Left shift result: {left_shift}")
print(f"Right shift result: {right_shift}")


Print the binary form before and after.
"""
print(f"Binary before shift: {bin(number)}")
print(f"Binary after left shift: {bin(left_shift)}")
print(f"Binary after right shift: {bin(right_shift)}")
