# 04. Fashion Boutique:
# LIFO - last in, first out

box_of_clothes = [int(i) for i in input().split()]
rack_capacity = int(input())

rack_counter = 1
sum_clothes = 0

while box_of_clothes:
    current_item = box_of_clothes.pop()
    if sum_clothes + current_item <= rack_capacity:
        sum_clothes += current_item
    else:
        rack_counter += 1
        sum_clothes = current_item

print(rack_counter)
