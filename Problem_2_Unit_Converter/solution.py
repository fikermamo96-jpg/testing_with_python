# your code here
def miles_to_kilometers(miles):
    return miles * 1.60934

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage:
miles = 10
kilometers = miles_to_kilometers(miles)
print(f"{miles} miles is {kilometers:.2f} kilometers.")

celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit:.2f}°F.")
