prices = [12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7] # сложность - o(n) + o(n)
kglob = 0
k = 1
list_k = [0] * (len(prices) + 2)
list_k[2] = 1
for i in range(3, len(list_k)):
    list_k[i] = i-1 + list_k[i-1] #заранее циклом создается список со значениями количества комбинаций подпоследовательностей разных длинн для обращения по индексу(индекс = длине)
for i in range(1, len(prices)):
    if (prices[i-1] - 1) == prices[i]:
        k += 1 #счетчик длины конкретной подпоследовательности
    elif k > 1:
        kglob += list_k[k] #общий счетчик количества подпоследовательностей
        k = 1
if k > 0:
    kglob += list_k[k]#вывод количества подпоследовательностей + все подпоследовательности длины 1, не учитывающиеся до этого
print(kglob, len(prices))