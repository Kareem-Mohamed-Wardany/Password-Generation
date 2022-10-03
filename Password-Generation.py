import string
import random

lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
digits = list(string.digits)

char_numbers = input("Enter number of characters you want to be generated: ")

while True:
    char_numbers = int(char_numbers)
    try:
        if char_numbers < 8:
            print("You need at least 8 characters")
            char_numbers = input("Please enter the number again: ")
        else:
            break
    except:
        print("You can enter numbers only")
        char_numbers = input("Please enter the number: ")

random.shuffle(lower_letters)
random.shuffle(upper_letters)
random.shuffle(digits)

number_of_letters = round(char_numbers * (25/100))
number_of_digits = round(char_numbers * (45/100))

password = []

for i in range(number_of_letters):
        password.append(lower_letters[i])
        password.append(upper_letters[i])

for i in range(number_of_digits):
        password.append(digits[i])

random.shuffle(password)
password = "".join(password[0:])

print(password)