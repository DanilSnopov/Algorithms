def square_counter(matrix): #сложность - o(n^2), где n - количество клеток
    counter_glob = 0
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1: #цикл проходит по матрице, начиная алгоритм подсчета, если находит еденицу
                    counter = 0
                    while (counter + i) < len(matrix) and (counter + j) < len(matrix[0]):#цикл проходит по правым и нижним граням квадратов, увеличивая размер квадрата с каждой итерацией
                        for i_ in range(0, counter):
                            if matrix[i + i_][j + counter] == 0:
                                counter = -1
                                break # если находится хоть один 0, то флаг назначается на -1, который одновременно и ограничивает дальнейшее выполнение второго цикла
                        for j_ in range(0, counter + 1):
                            if matrix[i + counter][j + j_] == 0:
                                counter = -1
                                break
                        if counter != -1:
                            counter_glob += 1 #если не было найдено ни одного нуля, то цикл продолжается
                        else:
                            break
                        counter += 1 #счетчик возвращается обратно
    return counter_glob
print(square_counter([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]))
