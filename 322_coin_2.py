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

        dp = [[amount+1 for i in range(amount + 1)] for j in range(lenc+1)]


        for i in range(1,lenc+1):
            for j in range(1,amount+1):
                #print(i,j)
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif j % coins[i-1] == 0:
                    dp[i][j] = j // coins[i-1]
                else:
                    c1 = dp[i][coins[i-1]]
                    tmp = j - coins[i-1]
                    c2 = dp[i][tmp]
                    #print(c1,c2)
                    if c1 > 0 and c2 > 0:
                        dp[i][j] = min(c1+c2,dp[i-1][j])
                    else:
                        dp[i][j] = dp[i-1][j]
        #print(dp[lenc])
        return dp[lenc][amount] if dp[lenc][amount] != amount +1 else -1
sol = Solution()
test_data = [
                # [ [1,2],3 ] ,
                # [ [1,3,4],5],
                 #[ [2,3,4],17],
                # [ [1,2,5],11],
                #[ [3,2],5],
                 #[ [1], 0 ],
                 [ [2], 3 ],
                 #[ [1], 2],
                 #[ [186,419,83,408],6249],
                 #[ [3,7,405,436],8839],
                 #[[470,18,66,301,403,112,360],8235],
                 #[[185,429,111,150,414,203,418],8197]
              ]
for d in test_data:
    print(sol.coinChange(d[0],d[1]))