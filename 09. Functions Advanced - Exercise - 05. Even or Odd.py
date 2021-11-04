# 05. Even or Odd:
def even_odd(*nums, even="", odd=""):
    if nums[0] == "even" or nums[0] == "odd":
        if nums[0] == "even":
            return [int(i) for i in even.split()]
        return [int(i) for i in odd.split()]

    if nums[0] % 2 == 0:
        return even_odd(*nums[1:], even=even + " " + str(nums[0]), odd=odd)
    return even_odd(*nums[1:], even=even, odd=odd + " " + str(nums[0]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 35, 100, "even"))