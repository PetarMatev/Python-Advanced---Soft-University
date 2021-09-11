# 01. Count Same Values:

numbers = tuple(map(float, input().split()))

nums_and_occurances = {}

for i in numbers:
    if i not in nums_and_occurances:
        nums_and_occurances[i] = 0
    nums_and_occurances[i] += 1

[print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]