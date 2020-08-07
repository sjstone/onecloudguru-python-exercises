def calculate(math_expression):
    numbers_and_operators = math_expression.split(" ")
    operator = numbers_and_operators[1]
    if operator == '+':
        return int(numbers_and_operators[0]) + int(numbers_and_operators[2])
    elif operator == '-':
        return int(numbers_and_operators[0]) - int(numbers_and_operators[2])
    elif operator == '*':
        return int(numbers_and_operators[0]) * int(numbers_and_operators[2])
    elif operator == '/':
        return int(numbers_and_operators[0]) / int(numbers_and_operators[2])
    else:
        print("Invalid mathematical operator.")


print(calculate("5 + 7"))
print(calculate("5 - 7"))
print(calculate("5 * 7"))
print(calculate("5 / 7"))
#TODO:  Need to handle these
#print(calculate("5.5 + 7.25"))
#print(calculate("5 / 0"))
