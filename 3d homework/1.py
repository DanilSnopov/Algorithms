def numEnclaves(grid: list) -> int: #сложность примерно о(н) или больше
        visited = set()
        qant = 0
        for i_ in range(len(grid)):
            for j_ in range(len(grid[0])): # проход по каждой клетке матрицы
                if grid [i_][j_] == 1:
                    if (i_, j_) not in visited:#если найден не замеченый ранее остров, начинается подсчёт
                        landarea = 0
                        flag = 0
                        stack = [(i_, j_)]
                        visited.add((i_, j_))
                        while stack and flag != 1:
                            landarea += 1
                            i, j = stack.pop()
                            if i-1 >= 0:
                                if grid[i-1][j] == 1:
                                    if (i-1, j) not in visited:
                                        stack.append((i-1, j))
                                        visited.add((i-1, j))
                            else:
                                flag = 1
                            if j-1 >= 0:
                                if grid[i][j-1] == 1:
                                    if (i, j-1) not in visited:
                                        stack.append((i, j-1))
                                        visited.add((i, j-1))
                            else:
                                flag = 1
                            if i+1 < len(grid):
                                if grid[i+1][j] == 1:
                                    if (i+1, j) not in visited:
                                        stack.append((i+1, j))
                                        visited.add((i+1, j))
                            else:
                                flag = 1
                            if j+1 < len(grid[0]):
                                if grid[i][j+1] == 1:
                                    if (i, j+1) not in visited:
                                        stack.append((i, j+1))
                                        visited.add((i, j+1))
                            else:
                                flag = 1
                        while stack: # если остров уже соприкоснулся с краем карты, дальше это можно не проверять
                            landarea += 1
                            i, j = stack.pop()
                            if i-1 >= 0:
                                if grid[i-1][j] == 1:
                                    if (i-1, j) not in visited:
                                        stack.append((i-1, j))
                                        visited.add((i-1, j))
                            if j-1 >= 0:
                                if grid[i][j-1] == 1:
                                    if (i, j-1) not in visited:
                                        stack.append((i, j-1))
                                        visited.add((i, j-1))
                            if i+1 < len(grid):
                                if grid[i+1][j] == 1:
                                    if (i+1, j) not in visited:
                                        stack.append((i+1, j))
                                        visited.add((i+1, j))
                            if j+1 < len(grid[0]):
                                if grid[i][j+1] == 1:
                                    if (i, j+1) not in visited:
                                        stack.append((i, j+1))
                                        visited.add((i, j+1))
                        if flag == 0: # если остров не соприкосался с краями карты
                            qant += landarea
        return qant
_ = 1
print(numEnclaves([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,_,_,_,0,0,0,0,0],
    [0,0,0,0,0,0,_,_,_,_,_,_,0,0,0],
    [0,0,0,0,_,_,_,_,0,0,_,_,_,0,0],
    [0,0,0,0,0,0,0,_,_,0,0,_,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]))
