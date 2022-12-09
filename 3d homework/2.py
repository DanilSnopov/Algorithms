def closedIsland(grid) -> int: # алгоритм очень похож на предыдущую задачу. Сложность такая же
        visited = set()
        qant = 0
        for i_ in range(len(grid)):
            for j_ in range(len(grid[0])):
                if grid [i_][j_] == 0:
                    if (i_, j_) not in visited:
                        flag = 0
                        stack = [(i_, j_)]
                        visited.add((i_, j_))
                        while stack and flag != 1:
                            i, j = stack.pop()
                            if i-1 >= 0:
                                if grid[i-1][j] == 0:
                                    if (i-1, j) not in visited:
                                        stack.append((i-1, j))
                                        visited.add((i-1, j))
                            else:
                                flag = 1
                            if j-1 >= 0:
                                if grid[i][j-1] == 0:
                                    if (i, j-1) not in visited:
                                        stack.append((i, j-1))
                                        visited.add((i, j-1))
                            else:
                                flag = 1
                            if i+1 < len(grid):
                                if grid[i+1][j] == 0:
                                    if (i+1, j) not in visited:
                                        stack.append((i+1, j))
                                        visited.add((i+1, j))
                            else:
                                flag = 1
                            if j+1 < len(grid[0]):
                                if grid[i][j+1] == 0:
                                    if (i, j+1) not in visited:
                                        stack.append((i, j+1))
                                        visited.add((i, j+1))
                            else:
                                flag = 1
                        while stack:
                            i, j = stack.pop()
                            if i-1 >= 0:
                                if grid[i-1][j] == 0:
                                    if (i-1, j) not in visited:
                                        stack.append((i-1, j))
                                        visited.add((i-1, j))
                            if j-1 >= 0:
                                if grid[i][j-1] == 0:
                                    if (i, j-1) not in visited:
                                        stack.append((i, j-1))
                                        visited.add((i, j-1))
                            if i+1 < len(grid):
                                if grid[i+1][j] == 0:
                                    if (i+1, j) not in visited:
                                        stack.append((i+1, j))
                                        visited.add((i+1, j))
                            if j+1 < len(grid[0]):
                                if grid[i][j+1] == 0:
                                    if (i, j+1) not in visited:
                                        stack.append((i, j+1))
                                        visited.add((i, j+1))
                        if flag == 0: # если остров ни разу не соприкоснулся с раницей карты
                            qant += 1
        return qant
print(closedIsland([
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0]]
))