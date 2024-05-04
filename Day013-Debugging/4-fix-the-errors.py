# Fix the Errors
# 由于 print 与 if 在同一级将报错
# 需要将 print 缩进一级 在 if 作用域中才可以
age = int(input("How old are you?"))
if age > 18:
print(f"You can drive at age {age}")