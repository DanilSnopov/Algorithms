def counter(values): #сложность - o(4n)
    h1 = 0 # h1 и h2 - 2 вершины, на которых стоят смотровые площадки
    max_val = 0
    for h2 in values: #цикл проходит по всем местам, каждый раз обновляя максимальную разницу между вершинами, левую вершину, и правую (правая сама является переменной цикла)
        max_val = max(h1 + h2, max_val)  # максимальная сумма вершин
        h1 = max(h1, h2) #если левая вершина с учетом расстояния менье правой, то она обновляется, и учитывается уже в следующей итерации
        h1 -= 1 # в переменной левой верины также автоматически хранится расстояние от левой вершины до правой
    return(max_val)
print(counter([8, 1, 5, 2, 6]))