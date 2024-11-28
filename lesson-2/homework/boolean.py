# 1.
username = input("Enter username: ")
password = input("Enter password: ")
print("Valid" if username and password else "Invalid")

# 2. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Equal" if a == b else "Not equal")

# 3. 
num = int(input("Enter a number: "))
print("Positive and even" if num > 0 and num % 2 == 0 else "Does not meet criteria")

# 4. 
nums = [int(input(f"Enter number {i+1}: ")) for i in range(3)]
print("All different" if len(set(nums)) == 3 else "Not all different")

# 5. 
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")
print("Same length" if len(text1) == len(text2) else "Different length")

# 6.
num = int(input("Enter a number: "))
print("Divisible by 3 and 5" if num % 3 == 0 and num % 5 == 0 else "Not divisible by 3 and 5")

# 7.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Greater than 50" if a + b > 50 else "Not greater than 50")

# 8.
num = int(input("Enter a number: "))
print("Between 10 and 20" if 10 <= num <= 20 else "Not in range")