def minimum(arr): # находит минимальные разности между рассортированными элементами и вписывает элементы с минимальной разностью в список
    arr = sorted(arr)
    mindiff = max(arr) - min(arr)
    pairs = []
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < mindiff:
            mindiff = abs(arr[i] - arr[i+1])
            pairs = [[arr[i], arr[i+1]]] # если найдена меньшая разность, список обнуляется
        elif abs(arr[i+1] - arr[i]) == mindiff:
            pairs.append([arr[i], arr[i+1]])
    return pairs
print(minimum([1, 5, 3, 8, 10]))