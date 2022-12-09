def getDecimalValue(head) -> int: #сложность о(н)
        bi = str(head.val)
        while head.next:
            head = head.next
            bi += str(head.val)
        return int(bi, 2)
            