def curcle_robber(nums): #сложность - o(2n)
    if len(nums) > 3:#при меньше чем 4 домах грабитель может ограбить только 1 дом
        maxdp = 0
        for i in range(2):
            num = nums[i:len(nums)+i-1]#грабитель не может ограбить и самый левый, и самый правый дом, значит можно посчитать лучшее для 2 вариантов
            dp = [0] * len(num)
            dp[0] = num[0]
            dp[1] = num[1]
            for i in range(2, len(num)):
                dp[i] = max(dp[i - 1], dp[i - 2] + num[i], dp[i - 3] + num[i]) #старый алгоритм ограбления домов с урока
            maxdp = max(dp[-1], maxdp)
        return maxdp
    elif nums:
        return max(nums)
    return 0
print(curcle_robber([0]))