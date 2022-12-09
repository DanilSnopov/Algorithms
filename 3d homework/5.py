def binaryTreePaths(root): # сложность - с * о(н)
        def waymaker(way, node): #проходит рекурсией по дереву, создавая вложенный список путей
            way += str(node.val) + '->'
            if node.left and node.right:
                return [waymaker(way, node.left), waymaker(way, node.right)]
            elif node.left:
                return waymaker(way, node.left)
            elif node.right:
                return waymaker(way, node.right)
            else:
                return way[:-2] #удаляет последнюю стрелочку
        def unpack(wayinp, way): #делает из вложенного списка обычный
            for i in wayinp:
                if type(i) == str:
                    way.append(i)
                else:
                    way += unpack(i, [])
            return way
        result = waymaker('',root)
        result = result if type(result) == list else [result]
        result = unpack(result, [])
        return result
            