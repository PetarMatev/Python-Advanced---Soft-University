# 05. Hot Potato:
from collections import deque

queue = deque(input().split(" "))

elimination = int(input())

while True:
    if len(queue) == 1:
        break
    for i in range(1, elimination + 1):
        person = queue.popleft()
        if i == elimination:
            print(f"Removed {person}")
        else:
            queue.append(person)

print(f"Last is {queue.popleft()}")
