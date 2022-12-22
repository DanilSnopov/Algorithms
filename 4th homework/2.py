class Solution: #не уверен, но возможно сложность o(n)
    def trimBST(self, root, low: int, high: int):
        while root.val < low or root.val > high:
            if root.val < low:
                if root.right:
                    root = root.right
                else:
                    return
            if root.val > high:
                if root.left:
                    root = root.left
                else:
                    return
        stack = [root] #корнем стала вершина, которая уже довлетворяет требованием и не имеет лишних веток
        while stack:
            node = stack.pop()
            if node.left:
                if node.left.val < low: #обработка ситуации, когда левая вершина меньше минимума. Находится ближайшая вершина, которая больше минимума, либо левая становится None
                    node2 = node.left
                    while node2.right:
                        node2 = node2.right
                        if node2.val >= low:
                            node.left = node2
                            break
                    else:
                        node.left = None
                if node.left:
                    stack.append(node.left)
            if node.right:
                if node.right.val > high: #симметрично левой
                    node2 = node.right
                    while node2.left:
                        node2 = node2.left
                        if node2.val <= high:
                            node.right = node2
                            break
                    else:
                        node.right = None
                if node.right:
                    stack.append(node.right)
        return root #всё