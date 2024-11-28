# 1. 
num = float(input("Enter a float number: "))
print(f"Rounded to 2 decimal places: {round(num, 2)}")

# 2. 
nums = [float(input("Enter a number: ")) for _ in range(3)]
print(f"Largest: {max(nums)}, Smallest: {min(nums)}")

# 3. 
km = float(input("Enter distance in kilometers: "))
print(f"Meters: {km * 1000}, Centimeters: {km * 100000}")

# 4. 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Division: {a // b}, Remainder: {a % b}")

# 5.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# 6.
num = int(input("Enter a number: "))
print(f"Last digit: {num % 10}")

# 7. 
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# 8. 
a = input("Enter first value: ")
b = input("Enter second value: ")
a, b = b, a
print(f"Swapped values: a = {a}, b = {b}")