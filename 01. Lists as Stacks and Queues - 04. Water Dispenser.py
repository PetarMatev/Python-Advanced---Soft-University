# 04. Water Dispenser:
from collections import deque

water_quantity = int(input())

queue = deque([])

while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

while True:
    instruction = input()
    if instruction == "End":
        break
    
    if "refill" in instruction:
        to_refill, amount = instruction.split(" ")
        water_quantity += int(amount)
    else:
        liters = int(instruction)
        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

print(f"{water_quantity} liters left")
