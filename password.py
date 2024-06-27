
import random
import string

alphabtes = string.ascii_letters
digits = string.digits
specialCharacters = string.punctuation

passwordChara = list(alphabtes + digits + specialCharacters)

def condition_random_password():
  length = input("Enter the Password Length: ")
  if int(length.isdigit()):
     alpha_count = input("Enter the Alphabtes Count in Password: " )
     if int(alpha_count.isdigit()):
        digits_count = input("Enter the Digits Count in Password: ")
        if int(digits_count.isdigit()):
            special_count = input("Enter the Special Characters Count: ")
            if int(special_count.isdigit()):
                    characters_count = int(alpha_count) + int(digits_count) + int(special_count)
                    if characters_count > int(length):
                        print("The entered Character Count is Greater than the total Password Length")
                        return
                    password = [] 
                    for i in range(int(alpha_count)):
                        password.append(random.choice(alphabtes))
                    for i in range(int(digits_count)):
                        password.append(random.choice(digits))
                    for i in range(int(special_count)):
                        password.append(random.choice(specialCharacters))
                    if characters_count < int(length):
                        random.shuffle(passwordChara)
                        for i in range(int(length) - characters_count):
                            password.append(random.choice(passwordChara))
                    print("".join(password))
            else:
              print("Enter a valid special count")
        else:
          print("Enter a valid digit count")
     else: 
       print('Enter a valid alpha count')
  else: 
    print("Enter a valid length")

def random_password():
  singlePassword = string.ascii_letters + string.digits + string.punctuation
  length = input("Enter the Password Length: ")
  if length.isdigit():
    print("".join(random.sample(singlePassword, int(length))))
  else:
    print("Please enter a valid length")

print("Please Select the below options \n ")
option = input("1 - Generating based on Conditions \n2 - Randomly Generating the Password \n Enter the Option: ")
if option == "1": 
  condition_random_password()
elif option == "2":
    random_password()
else:
  print("Invalid Option")
