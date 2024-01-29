programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as excepted.",
    "Function":"A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
# 从字典中查找元素
print(programming_dictionary["Bug"]);

# Edit an item in a dictionary
# 编辑字典中的元素
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

# Adding new items to dictionary
# 添加新元素到字典中
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Loop through a dictionary
# 遍历字典
for key in programming_dictionary:
    print(key)
    print(f"  {programming_dictionary[key]}")
    
# Create an empty dictionary.
# 创建一个空字典
empty_dictionary = {}

# Wipe an existing dictionary
# 擦除现有字典
programming_dictionary = {}
print(programming_dictionary)