# 04. Chairs:
def combinations(names, count, combs=[]):
    if len(combs) == count:
        return print((', '.join(combs)))

    for i in range(len(names)):
        combs.append(names[i])
        combinations(names[i+1:], count, combs)
        combs.pop()

    return

combinations(input().split(", "), int(input()))