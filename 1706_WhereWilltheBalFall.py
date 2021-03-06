from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        fin = -1
        res = []
        width = len(grid[0])
        height = len(grid)
        def dfs(y,x):
            #print(x,y)

            if y == height-1:
                self.fin = x
                #print("fin", self.fin,x, y)
                return
            if grid[y+1][x] == 1:
                if x+1 < width and grid[y+1][x] == grid[y+1][x+1]:
                    dfs(y+1,x+1)
            if grid[y+1][x] == -1:
                if x-1 >=0 and grid[y+1][x] ==grid[y+1][x-1]:
                    dfs(y+1,x-1)

        for i in range(width):
            self.fin = -1
            dfs(-1,i)
            res.append(self.fin)
            #print("--"*10)
        return res


print(Solution().findBall(grid = [[ 1, 1, 1,-1,-1],
                                  [ 1, 1, 1,-1,-1],
                                  [-1,-1,-1, 1, 1],
                                  [ 1, 1, 1, 1,-1],
                                  [-1,-1,-1,-1,-1]]))

print(Solution().findBall(grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))