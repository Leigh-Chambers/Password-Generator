#Password Generator
import random
#Alphabet, number, symbol lists (Could use ascii function to refine.)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Let's generate secure password for you!")
nr_letters= int(input("How many letters are required in your new your password?\n")) 
nr_symbols = int(input(f"And how many symbols are needed?\n"))
nr_numbers = int(input(f"How many numbers would are required?\n"))

#Create empty list.
password=[]
#Iterate through, randomly choosing letters, numbers and symbols for the password and adding them into the list.
for i in range (0, nr_letters):
  password.append(random.choice(letters))

for j in range(0, nr_symbols):
  password.append(random.choice(symbols))
  
for k in range(0, nr_numbers):
  password.append(random.choice(numbers))

#Randomly shuffle the result of the list.
random.shuffle(password)
#Turn the list into a string 
print("".join(password))