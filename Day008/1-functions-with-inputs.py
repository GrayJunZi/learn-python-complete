# 函数

def greet():
    print("Hello")

greet()

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Angela")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jack", "Shanghai")
greet_with(location="nowhere", name="owe")
