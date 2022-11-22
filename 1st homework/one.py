def stepcounter(numb): #простая функция, которая просто следует алгоритму из условия. Сложность log(n)
    kol = 1
    while numb > 1:
        if numb % 2 !=0:
            numb -= 1
            kol+=1
        numb //= 2
        kol += 1
    return kol
print(stepcounter(14))