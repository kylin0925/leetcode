class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """

        # N = 10
        # K = 2
        # W = 2
        if K == 0 or K + W <= N:
            return 1.0
        dp = [0.0 for i in range(N + 1)]

        dp[0] = 1.0
        res = 1

        for i in range(1, N + 1):
            dp[i] = dp[i - 1]
            if i <= W:
                dp[i] += (dp[i - 1]) / W
            else:
                dp[i] += (dp[i - 1] - dp[i - W - 1]) / W
            if i > K:
                dp[i] -= (dp[i - 1] - dp[K - 1]) / W
        res = 0

        return (dp[N] - dp[K - 1])

sol = Solution()
test_data = [[4,2,2],[10,1,10],[6,1,10],[21,17,10],[1,0,1]]
for d in test_data:
    print(sol.new21Game(d[0],d[1],d[2]))
