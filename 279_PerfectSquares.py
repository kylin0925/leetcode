class Solution:
    def numSquares(self, n: int) -> int:

        maxsq = int(n**0.5)
        tbl = [[0 for i in range(n+1)] for j in range(maxsq+1)]
        tbl[1] = [i for i in range(n+1)]

        for p in range(2,maxsq+1):
            p2 = p**2
            for i in range(1, n+1):
                if i < p2:
                    tbl[p][i] = tbl[p-1][i]
                else:
                    r = i - p2
                    c = tbl[p][r] + 1
                    tbl[p][i] = min(c, tbl[p-1][i])
        #print(tbl)
        return tbl[maxsq][n]


print(Solution().numSquares(12))
print(Solution().numSquares(16))
# print(Solution().numSquares(21))
# print(Solution().numSquares(999))
import time
start = time.time()
print(Solution().numSquares(10000))
print(time.time() - start)
# print(Solution().numSquares(1234))

