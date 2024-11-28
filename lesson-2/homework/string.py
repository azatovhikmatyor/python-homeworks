# 1. 
sentence = input("Enter a sentence: ")
print(sentence.title())

# 2. 
text = input("Enter a string: ")
print("".join([char for char in text if char.lower() not in "aeiou"]))

# 3. 
text = input("Enter a string: ")
print(text[::-1])

# 4. 
text = input("Enter a string: ")
print(text.replace(" ", "_"))

# 5. 
word = input("Enter a word: ")
print("Palindrome" if word == word[::-1] else "Not a palindrome")

# 6. 
text = input("Enter a string: ")
print(text.replace("a", "o"))

# 7. 
email = input("Enter an email: ")
print(f"Username: {email.split('@')[0]}")

# 8.
text = input("Enter a string: ")
print(text.title())

# 9. 
text = input("Enter a string: ")
print(text[1:-1])

# 10. 
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
print("Present" if word in sentence else "Not present")

# 11.
text = input("Enter a string: ")
char = input("Enter a character: ")
print(text.find(char))

# 12.
text = input("Enter a string: ")
print(text[-3:])

# 13. 
text = input("Enter a string: ")
count = int(input("How many times to repeat? "))
print(text * count)

# 14. 
sentence = input("Enter a sentence: ")
for word in sentence.split():
    print(word)

# 15. 
text = input("Enter a string: ")
print(text[1::2])

# 16. 
text = input("Enter a string: ")
print(f"Title: {text}")

# 17. 
sentence = input("Enter a sentence: ")
print(" ".join(sentence.split()[::-1]))

# 18. 
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")
print(abs(len(text1) - len(text2)))