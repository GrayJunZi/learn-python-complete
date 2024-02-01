# Calculator

# Add
def add(n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1,n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calculator():
    print(logo)
    num1 = float(input("第一个数字是什么?: "))

    print([symbol for symbol in operators])

    should_continue = True
    while should_continue:
        operation_symbol = input("选择一个操作: ")
        num2 = float(input("下一个数字是什么?: "))
        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"输入 'y' 继续计算 {answer}, 或者输入 'n' 开始一个新的计算: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()