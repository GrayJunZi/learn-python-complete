import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like?\n"))
number = int(input("How many numbers would you like?\n"))

password = ''

for i in range(0, letter):
    password += letters[random.randint(0, len(letters)-1)]

for i in range(0, symbol):
    password += symbols[random.randint(0, len(symbols)-1)]

for i in range(0, number):
    password += numbers[random.randint(0, len(numbers)-1)]

print(f"{password}")

password_list = []

for i in range(0, letter):
    password_list.append(random.choice(letters))

for i in range(0, symbol):
    password_list.append(random.choice(symbols))

for i in range(0, number):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(f"You password is: {str.join('', password_list)}")

