from sympy.physics.units import length
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator\n")
length_of_password=int(input())
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]

if length_of_password==nr_letters+nr_symbols+nr_numbers:
    for i in range(0,nr_letters):
        password.append(r.choice(letters))
    for i in range(0,nr_symbols):
        password.append(r.choice(symbols))
    for i in range(0,nr_numbers):
        password.append(r.choice(numbers))

r.shuffle(password)

final_password=''.join(password)

print(final_password)


