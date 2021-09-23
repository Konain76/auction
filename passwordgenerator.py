import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
password_l = ""
password_s = ""
password_n = ""
for x in range(0, nr_letters):
    password_l += random.choice(letters)
for y in range(0, nr_symbols):
    password_s += random.choice(symbols)
for z in range(0, nr_numbers):
    password_n += random.choice(numbers)
password = password_l + password_s + password_n
print(password)
password = list(password)
print(password)
random.shuffle(password)
print(password)
final = ""
for n in password:
    final += n
print(f" your stong password is : {final}")