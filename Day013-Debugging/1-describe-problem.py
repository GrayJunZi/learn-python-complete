# descibe problem
# 将不会输出 You got it，因为循环的范围是 1 - 19，不会输出到20
# 需要将 range(1, 20) 改为 range(1, 21)
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
my_function()