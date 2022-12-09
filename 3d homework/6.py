def diameterOfBinaryTree(root) -> int:# сложность - 2*о(n)
        def deepcouter(node): # рекурсивная функция проходит по дереву, высчитывая высоту каждой вершин над листком
            if node.left and node.right:
                val = max(deepcouter(node.left), deepcouter(node.right)) + 1
                node.val = val
                return val
            elif node.right:
                val = deepcouter(node.right) + 1
                node.val = val
                return val
            elif node.left:
                val = deepcouter(node.left) + 1
                node.val = val
                return val
            else:
                node.val = 0
                return 0
        deepcouter(root)
        globstack = [root]
        max_depth = root.val #если дерево не ветвится
        while globstack:# обход в глубину, вычисляется самое глубокое сочетание 2 вершин
            node = globstack.pop()
            if node.left and node.right:
                globstack.append(node.left)
                globstack.append(node.right)
                max_depth = max(node.left.val + node.right.val + 2, max_depth)
            elif node.left:
                globstack.append(node.left)
            elif node.right:
                globstack.append(node.right)
        return max_depth