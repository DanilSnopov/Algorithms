def power(x): #функция находит мощность числа
    pow = 0
    while x > 1:
        if x == 16:
            pow += 4
            break
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
        pow += 1
    return pow
powers = []
lo, hi, k = int(input('c')), int(input('по')), int(input('какой по счету'))
for i in range (lo, hi+1):
    powers.append((power(i)))
powers_2 = sorted(powers) # создан список мощностей отрезка чисел и отсортированный список с теми же элементами
numbers = []
for i in range(len(powers_2)): # создается список чисел, отсортированный по их мощностям 
    numbers.append(powers.index(powers_2[i])+lo)
    powers[powers.index(powers_2[i])] = -1
print(numbers[k-1]) # выводится нужное число
