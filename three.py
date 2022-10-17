def func(jewels, stones):
    my_jewels = 0
    for stone in stones:
        if stone in jewels:
            my_jewels += 1
    return my_jewels
print(func("AfG", "HGBkseFFffuhfguybUOVUTRA"))