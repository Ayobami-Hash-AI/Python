# AyobamiFunction.py

def count_letters(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)


# Get input from user
user_input = input("Enter a string: ")

# Call the function
count_letters(user_input)