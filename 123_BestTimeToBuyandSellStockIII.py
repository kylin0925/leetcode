from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_price = len(prices)
        dp = [[0 for j in range(num_price + 1)] for i in range(3)]

        minp = [0,-prices[0],-prices[0]]
        for j in range(1, num_price):
            for i in range(1, 3):
                dp[i][j] = max(dp[i][j-1],prices[j] + minp[i] )
                minp[i] = max(minp[i], dp[i-1][j-1] -prices[j] )
        print(dp);
        return dp[2][num_price - 1]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        num_price = len(prices)
        # dp = [[0 for j in range(num_price + 1)] for i in range(3)]

        p1 = -prices[0]
        p2 = -prices[0]

        dp0 = 0
        dp1 = 0
        dp2 = 0
        for j in range(1, num_price):
            # for i in range(1, 3):
            dp1 = max(dp1, prices[j] + p1)
            p1 = max(p1, -prices[j])

            dp2 = max(dp2, prices[j] + p2)
            p2 = max(p2, dp1 - prices[j])
        # print(dp);
        return dp2
sol = Solution2()
print(sol.maxProfit(prices = [3,3,5,0,0,3,1,4]))
print(sol.maxProfit(prices = [1,2,3,4,5]))
# print(sol.maxProfit(prices = [0,1,0,3,4,5]))
# print(sol.maxProfit(prices = [0]))
# print(sol.maxProfit(prices = [1,1,2,2]))
# print(sol.maxProfit(prices = [1,2]))
# print(sol.maxProfit(prices = [0,0,0,7,1,2,3,1,1,9,10,11]))
# print(sol.maxProfit(prices = [0,7,1,11]))
