# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for i in range(nr_letters):
#    password += (letters[(i*i)*nr_letters % 52])
# for i in range(nr_symbols):
#    password += (symbols[(i*i)*nr_letters % 9])
# for i in range(nr_numbers):
#    password += (numbers[(i*i)*nr_letters % 10])
# print("Your Password: " + str(password))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
for i in range(nr_letters):
    password += (letters[random.randint(0, nr_letters)*nr_letters % 52])
for i in range(nr_symbols):
    password += (symbols[random.randint(0, nr_symbols)*nr_symbols % 9])
for i in range(nr_numbers):
    password += (numbers[random.randint(0, nr_numbers)*nr_numbers % 10])
l = list(password)
random.shuffle(l)
shuffledpassword = ''.join(l)
print("Your Password: " + shuffledpassword)
