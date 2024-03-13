
import random
import string

def generate_password(length, include_upper, include_lower, include_digits, include_symbols):

  characters = ""
  if include_upper:
    characters += string.ascii_uppercase
  if include_lower:
    characters += string.ascii_lowercase
  if include_digits:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  if not characters:
    print("Error: Please select at least one character type.")
    return None


  password_list = list(characters)
  random.shuffle(password_list)


  password = ''.join(password_list[:length])
  return password

while True:

  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length < 8:
      print("Password length must be at least 8 characters.")
      continue

    include_upper = input("Include uppercase letters (y/n)? ").lower() == 'y'
    include_lower = input("Include lowercase letters (y/n)? ").lower() == 'y'
    include_digits = input("Include digits (y/n)? ").lower() == 'y'
    include_symbols = input("Include symbols (y/n)? ").lower() == 'y'
  except ValueError:
    print("Invalid input. Please enter a number for password length.")
    continue


  password = generate_password(length, include_upper, include_lower, include_digits, include_symbols)
  if password:
    print(f"Your generated password is: {password}")

  
  user_choice = input("Generate another password? (y/n): ")
  if user_choice.lower() != 'y':
    break

print("Thank you for using my password generator!")