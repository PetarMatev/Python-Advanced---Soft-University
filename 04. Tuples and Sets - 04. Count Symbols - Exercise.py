# 04. Count Symbols:
info = tuple(i for i in input())
repeated = []
for i in range(len(info)):
    info = sorted(info)
    if info[i] not in repeated:
        print(f"{info[i]}: {info.count(info[i])} time/s")
    repeated.append(info[i])

