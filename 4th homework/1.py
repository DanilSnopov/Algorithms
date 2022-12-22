class Solution: #сложность между o(n) и o(n^2)
    def findLongestChain(self, pairs) -> int:
        pairs = sorted(pairs) #сначала сортировка по первому элементу
        dp = [1]* (len(pairs))
        for i in range(1, len(pairs)): #проход по всем парам последовательности
            n = 70 #именно такого количества хватает на все случаи
            if i < n:
                n = i
            for j in range(i-1, i-1-n, -1): #выбираю лучший вариант для текущей i-й пары из 70 предыдущих
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1) 
        return dp[-1]#в последнем элементе лучший результат