# 4.	Mathematical operations
# Create a module that does basic calculations. You will receive 2 numbers and a sign between them all in one string:

def math_operations(data):
    result = 0
    number1, sign, number2 = data.split()
    number1 = float(number1)
    number2 = int(number2)

    possible_signs = ["/", "*", "-", "+", "^"]

    if sign in possible_signs:

        if sign == "/":
            result = number1 / number2
        elif sign == "*":
            result = number1 * number2
        elif sign == "-":
            result = number1 - number2
        elif sign == "+":
            result = number1 + number2
        elif sign == "^":
            result = number1 ** number2
        result = f"{result:.2f}"
        return result
