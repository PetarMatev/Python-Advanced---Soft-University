# 05. Operate:

def operate(sign, *numbers):

    result = numbers[0]
    for num in numbers[1:]:

        if sign == "+":
            result += num
        elif sign == "-":
            result -= num
        elif sign == "*":
            result *= num
        elif sign == "/":
            result /= num

    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

