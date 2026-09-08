import random
import string 


#Password Generator

alphabet = string.ascii_lowercase

password = ""

uppercase_letters = input("Do you want uppercase letters? ")

if uppercase_letters.strip().lower() == "yes":

    alphabet += string.ascii_uppercase


numbers = input ("Do you want numbers? ")

if numbers.strip().lower() == "yes":

    alphabet += string.digits

symbols = input ("Do you want symbols? ")

if symbols.strip().lower() == "yes":

    alphabet += string.punctuation 

valid_input = False

while valid_input == False:
    password_length = input("How long do you want your password to be? ")

    try: 
        password_length = int(password_length)

        valid_input = True

    except ValueError:

        print ("Please enter a valid number")

for i in range (password_length):
        
    password += random.choice(alphabet)



# Strength Checker


#Checks if password has a lowercase letter anywhere in it

found_lowercase = False

for char in password:

    if char.islower():

        found_lowercase = True 

    
if found_lowercase:

    print ("Contains Lowercase: YES")

else:

    print ("Contains Lowercase: NO")

#Checks if password has an uppercase letter anywhere in it


found_uppercase = False

for char in password:

    if char.isupper():

        found_uppercase = True

if found_uppercase:

    print ("Contains Uppercase: YES")

else:

    print ("Contains Uppercase: NO")

#Checks if password has a number anywhere in it

found_numbers = False

for char in password:

    if char.isdigit():

        found_numbers = True

if found_numbers:

    print ("Contains Numbers: YES")

else:

    print ("Contains Numbers: NO")


#Checks if password has symbols anywhere in it

found_symbols = False

for char in password:

  if char in string.punctuation:

    found_symbols = True

if found_symbols:

    print ("Contains Symbols: YES")

else:

    print("Contains Symbols: NO")


print (f"This is your password: {password}")


#Calculate Password Strength

score = 0 

if found_lowercase: score += 1
if found_uppercase: score += 1
if found_numbers:   score += 1
if found_symbols:   score += 1

#Adds a point's depending on the password length

if len (password) >= 8:

    score += 1

if len (password) >= 12:

    score += 2

if len (password) >= 16:

    score += 3

print("\n--- PASSWORD STRENGTH ---")

if score <= 2:

    print ("Password strength: WEAK")

elif score <= 4:

    print ("Password strength: MODERATE")

elif score <= 6:

    print ("Password strength: STRONG")

else:

    print ("Password strength: VERY STRONG")