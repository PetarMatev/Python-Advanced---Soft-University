# 04. Parking Lot:
numbers = int(input())
parking_lot = set()

for i in range(numbers):
    command = input().split(", ")
    direction, car_number = command

    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        parking_lot.remove(car_number)


if len(parking_lot) > 0:
    [print(item) for item in parking_lot]
else:
    print("Parking Lot is Empty")


