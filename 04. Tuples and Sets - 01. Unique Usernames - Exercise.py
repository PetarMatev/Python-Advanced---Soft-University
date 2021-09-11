# 01. Unique Usernames:
num = int(input())
info = set()

for i in range(num):
    info.add(input())

[print(name) for name in info]