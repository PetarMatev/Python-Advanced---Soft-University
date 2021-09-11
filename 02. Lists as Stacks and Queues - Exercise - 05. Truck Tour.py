# 05. Truck Tour:
from collections import deque
n = int(input())
outcome = 0
tank = 0
queue = deque([])

for i in range(n):
    petrol, distance = [int(j) for j in input().split()]
    tank += petrol

    if distance <= tank:
        tank -= distance
    else:
        tank = 0
        outcome = i + 1

while queue:
    petrol_p = queue[0]
    distance_d = queue[1]

    tank += petrol_p

    if distance_d <= tank:
        tank -= distance_d
        queue.popleft()
        queue.popleft()

print(outcome)
