import time
import random
list = []
up_to = int(input('длина списка:'))
for i in range(up_to):
    list.append(random.randint(-99999999999, 99999999999))

def func(nums, k):
    nums = sorted(nums)
    return nums[len(nums) - k]

how_much = int(input('какой по счету максимальный элемент:'))
starttime = time.time()
print(func(list, how_much))
print((time.time() - starttime)*1000, 'млс')