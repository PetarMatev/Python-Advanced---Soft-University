# 02. Odd or Even:
def odd_or_even(command, numbers, even=0, odd=0, counter=0):
    if not numbers:
        if command == "Odd":
            return odd * counter
        else:
            return even * counter

    if numbers[0] % 2 != 0:
        return odd_or_even(command, numbers[1:], even, odd + numbers[0], counter + 1)
    return odd_or_even(command, numbers[1:], even + numbers[0], odd, counter + 1)


print(odd_or_even(input(), list(map(int, input().split()))))
