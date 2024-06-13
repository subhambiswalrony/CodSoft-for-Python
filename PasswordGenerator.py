# write a program to Create a Password Generator by taking user's desired length
import random

capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallLetters = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
specialCharacters = "!@#$%^&*()"

password = capitalLetters + smallLetters + number + specialCharacters
passwordLength = int(input("Enter your length of the password: "))

generatedPassword = "".join(random.sample(password, passwordLength))

print("Your generated password for required length", passwordLength, "is: ", generatedPassword)