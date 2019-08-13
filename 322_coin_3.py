class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        coins.sort()
        self.min_coin = 0
        lenc = len(coins)

        dp = [amount+1 for i in range(amount + 1)]

        dp[0] = 0
        for i in range(lenc):
            for j in range(1,amount+1):
                if j >= coins[i]:
                    tmp = j - coins[i]
                    c2 = dp[tmp]
                    #print(c1,c2)
                    dp[j] = min(c2 +1 ,dp[j])
                #print(coins[i], j, dp)
        #print(dp)
        return dp[amount] if dp[amount] != amount +1 else -1
sol = Solution()
test_data = [
                 [ [1,2],3 ] ,
                 # [ [1,3,4],5],
                 # [ [2,3,4],17],
                 # [ [1,2,5],11],
                 # [ [3,2],5],
                 # [ [1], 0 ],
                  [ [2], 3 ],
                  [ [1], 2],
                  [ [186,419,83,408],6249],
                  [ [3,7,405,436],8839],
                  [[470,18,66,301,403,112,360],8235],
                  [[185,429,111,150,414,203,418],8197]
              ]
for d in test_data:
    print(sol.coinChange(d[0],d[1]))