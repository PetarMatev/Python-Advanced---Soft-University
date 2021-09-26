# 06. Battle of Names:
num = int(input())
odd_set = set()
even_set = set()

for i in range(1, num + 1):
    outcome = sum([ord(i) for i in input()]) // i
    if outcome % 2 == 0:
        even_set.add(outcome)
    else:
        odd_set.add(outcome)

if sum(odd_set) == sum(even_set):
    print(", ".join([str(i) for i in (odd_set | even_set)]))

if sum(odd_set) > sum(even_set):
    print(", ".join([str(i) for i in (odd_set - even_set)]))

if sum(odd_set) < sum(even_set):
    print(", ".join([str(i) for i in (odd_set ^ even_set)]))



