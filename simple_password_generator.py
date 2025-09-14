import random
import string

# This 'while' loop asks the user for a valid password length ubntil they give one
while True:
    try:
        # The code below asks the user for inpout and converts it into an integer
        length = int(input("Enter password length: "))

        #  Check that the length is at least 3 characters
        if length < 3:
            print("Password length must be at least 3!")
        else:
            # If valid, break out of the loop
            break
    except ValueError:
        #  If the user types something that's not a number, show an error message
        print("Please enter a valid number!")

# These variables now hold all the characters we can use
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

password_chars = [random.choice(letters), random.choice(digits), random.choice(symbols)]

# Combine all character sets
# This makes one big string containing all possible characters we want to use for the password
all_chars = letters + digits + symbols

# Pick the remaining characters randomly to reach the desired length
# 'random.choices()' picks 'k' random elements from a sequence with replacement.

# 'length-3' ensures we fill the password up to the user's desired length, since we 
# already have 3 characters guaranteed (1 letter, 1 digit, 1 symbol).

# 'password_chars += ...' adds the newly picked characters to the list 'password_chars'.
# After this step, 'password_chars' contains all the characters for the password, but the first 
# three are always letter, then digit, then symbol.
password_chars += random.choices(all_chars, k=length-3)

# the code below is to shuffle the list in place
random.shuffle(password_chars)

# ' "".join(password_chars) ' takes all those list items and joins them into one string with no spaces in between
# The result gets stored in the variable "password".
password = "".join(password_chars)

print(f'Your password is: {password}')