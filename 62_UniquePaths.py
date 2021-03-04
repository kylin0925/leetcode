class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        pathMap = [ [0 for x in range(n)] for y in range(m)]

        for i in range(n):
            pathMap[0][i] = 1
        for i in range(m):
            pathMap[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                pathMap[i][j] =pathMap[i][j-1] +pathMap[i-1][j]

        return pathMap[m-1][n-1]

sol = Solution()
print(sol.uniquePaths(3,7))

#2000000000
#1677106640
#571350360240