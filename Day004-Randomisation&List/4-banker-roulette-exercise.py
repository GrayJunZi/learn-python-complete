#  谁来买单程序练习

import random

name_string = input("Give me everybody's names, seperated by a comma.")

names = name_string.split(', ')

number = random.randint(0, len(names)-1)
print(f"{names[number]} is going to buy the meal today!")

print(random.choice(names))
