# 07. Robotics:
from collections import deque
from datetime import datetime, timedelta


text = list(input().split(";"))
starting_time = input()


queue = deque([])
robots_and_time = []

while True:
    command = input()
    if command == "End":
        break
    queue.append(command)

for i in range(len(text)):
    robot = text[i]
    robots_and_time.append(robot)
    robots_and_time.append(starting_time)

while queue:
    item = queue[0]
    hh, mm, ss = starting_time.split(":")
    ss = str(int(ss) + 1)
    starting_time = hh + mm + ss
    z = starting_time
    for i in range(1, len(robots_and_time) + 1):
        if i % 2 != 0:
            robot_on_line = robots_and_time[i - 1]
            robot_time = robots_and_time[i]
            if robot_time == starting_time:
                print(f"{robot_on_line} - {item} [{robots_and_time[i]}]")
                queue.popleft()
                break
