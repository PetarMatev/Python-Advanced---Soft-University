def Fibonacci(n):
    basket = []

    if n == 0:
        return 0
    elif n == 1:
        return 0

    current = 0
    previous = 0
    while len(basket) < n:
        if current == 0:
            basket.append(current)
            previous = current
            current = current + 1
        elif current == 1 and len(basket) < 3:
            basket.append(current)
            previous = current
            current = 1
        else:
            temporary = current + previous
            previous = current
            current = temporary
            basket.append(current)

    return basket
