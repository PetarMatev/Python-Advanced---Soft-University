# 03. Fast Food:
from collections import deque

quantity_of_food = int(input())
quantity_of_orders = deque([int(i) for i in input().split()])
biggest_order = max(quantity_of_orders)

food_still_available = True

while len(quantity_of_orders) > 0:
    current_order = quantity_of_orders[0]
    if quantity_of_food < current_order:
        food_still_available = False
        break
    quantity_of_orders.popleft()
    quantity_of_food -= current_order

print(biggest_order)
if food_still_available:
    print("Orders complete")
else:
    quantity_of_orders = [str(i) for i in quantity_of_orders]
    print(f"Orders left: {' '.join(quantity_of_orders)}")
