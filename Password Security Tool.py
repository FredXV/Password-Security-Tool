import random
import string 


#Password Generator

alphabet = string.ascii_lowercase

password = ""

uppercase_letters = input("Do you want uppercase letters? ")

if uppercase_letters == "yes":

    alphabet += string.ascii_uppercase


numbers = input ("Do you want numbers? ")

if numbers == "yes":

    alphabet += string.digits

symbols = input ("Do you want symbols? ")

if symbols == "yes":

    alphabet += string.punctuation 

    
for i in range (int(input("How long do you want your password to be? "))):

    password += random.choice(alphabet)


print (f"\nGenerated Password: {password}")

print (f"Password Length: {len(password.strip())} characters")


print(f"Password Length: {len(password.strip())} characters") 

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

