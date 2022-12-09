def averageOfLevels(root): # сложность о(н)
        stack = [(root, 0)]
        itog = []
        cur_depth = 0
        summ = 0
        kol = 0
        while stack:
            node, depth = stack.pop(0) #обход в ширину
            if depth > cur_depth: # с погружением на 1 глубже каждый раз пере менные обновляются
                itog.append(summ / kol)
                summ, kol = 0, 0
                cur_depth = depth
            summ += node.val
            kol += 1
            if node.left:
                stack.append((node.left, cur_depth + 1))
            if node.right:
                stack.append((node.right, cur_depth + 1))
        return itog + [summ / kol] # добавляется последнее значение, не вошедшее сюда вов ремя цикла