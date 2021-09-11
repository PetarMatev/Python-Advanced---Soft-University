# 05. Longest Intersection:
num = int(input())
info = []

for i in range(num):
    left, right = input().split("-")
    left_start, left_finish = left.split(",")
    right_start, right_finish = right.split(",")

    left_range = set([int(i) for i in range(int(left_start), int(left_finish) + 1)])
    right_range = set([int(i) for i in range(int(right_start), int(right_finish) + 1)])

    current_intersection = set.intersection(left_range, right_range)
    if len(current_intersection) > len(info):
        info = current_intersection

print(f"Longest intersection is {[i for i in info]} with length {len(info)}")


