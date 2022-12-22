class Solution: 
    def minDistance(self, word1: str, word2: str) -> int:# cложность 2o(n) + o(n^2)
        l1, l2 = [], []
        for i in word1:
            l1.append(i)
        for i in word2:
            l2.append(i)
        k = 0
        for a in l1:
            if not (a in l2):
                l1.remove(a)
                k += 1
        for a in l2:
            if not (a in l1):
                l2.remove(a)
                k += 1 #все лишние буквы удалены и подсчитаны
        if len(l1) * len(l2) == 0:
            return k #если все буквы были лишними
        dp = []
        for i in range(len(l1) + 1):
            dp.append([0] * (len(l2) + 1))#формирование дп
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i] == l2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return len(l1) -dp[-2][-2] + len(l2) - dp[-2][-2] + k #в дп зранится максимальная длина общей подпоследовательности обоих списков