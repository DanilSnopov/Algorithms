import time
import random
list = []
up_to = int(input('длина списка:'))
for i in range(up_to):
    list.append(random.randint(-99999999999, 99999999999))

def func(nums, k):
    maxes = [int(min(nums))] * k
    kmin = 0
    index = 0
    for i in nums:
        if i > kmin:
            maxes[index] = i
            index = maxes.index(min(maxes))
            kmin = maxes[index]
    return min(maxes)
how_much = int(input('какой по счету максимальный элемент:'))
starttime = time.time()
print(func(list, how_much))
print(time.time() - starttime)