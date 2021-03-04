from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ylen = len(grid)
        xlen = 0
        print(grid,ylen,xlen)
        if ylen > 0:
            xlen = len(grid[0])

        costmap = [ [0 for i in range(xlen * ylen)] for j in range(xlen * ylen)]

        nodecnt = ylen * xlen
        print(costmap)

sol = Solution()
sol.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])