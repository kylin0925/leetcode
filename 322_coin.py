class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount ==0:
            return 0
        coins.sort()
        coins = coins[::-1]

        self.min_coin = -1
        lenc = len(coins)

        def dfs(start,r,n):

            if not r:
                if self.min_coin == -1 or self.min_coin > n:
                    self.min_coin = n
                    #print("count",n)
            #print(n)
            for i in range(start,lenc):
                if r >= coins[i]:
                    #print(r,coins[i],self.min_coin , n)
                    if self.min_coin == -1 or r < coins[i] * (self.min_coin - n):
                        dfs(i,r - coins[i],n+1)
        #for i in range(lenc):
        dfs(0,amount,0)
        return self.min_coin
sol = Solution()
test_data = [
                [ [1,2],3 ] ,
                [ [1,3,4],5],
                [ [1,2,5],11],
                [ [3],5],
                [ [1], 0 ],
                [ [1], 2],
                [ [186,419,83,408],6249],
                [ [3,7,405,436],8839],
                [[470,18,66,301,403,112,360],8235],
                [[185,429,111,150,414,203,418],8197]
              ]
for d in test_data:
    print(sol.coinChange(d[0],d[1]))