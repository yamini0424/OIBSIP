try:
 import random
 import string 
 length = int(input("Enter password length: "))
 if length <= 0:
    print("enter the number greater than zero") 
 else:
  letters = input("Include letters? (y/n): ").lower()
  numbers = input("Include numbers? (y/n): ").lower()
  symbols = input("Include symbols? (y/n): ").lower()
  characters=""
  if letters=="y":
    characters += string.ascii_letters
  if numbers=="y":
    characters += string.digits
  if symbols == "y":
    characters += string.punctuation
  if characters=="":
    print("Please enter atleast one character type")
  else:
    password=""
    for i in range (length):
      password +=random.choice(characters)
    print("Generated password = ",password)
except ValueError:
   print("Invalid input! Please enter the valid input.")    
    

