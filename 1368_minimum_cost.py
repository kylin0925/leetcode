import collections
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # r l d u
        dir = [ [1, 0], [-1, 0], [0, 1], [0, -1]]

        m = len(grid)
        n = len(grid[0])

        visited = {}
        queue = collections.deque([(0,0)])
        cost_map = [[1000000000 for x in range(n)] for y in range(m) ]
        x = y = 0
        cost_map[0][0] = 0
        while queue:
            x, y = queue.popleft()

            #print(x,y)
            dx=x
            dy=y
            cost = cost_map[y][x]
            while 0<=dx<n and 0<=dy<m and (dx,dy) not in visited:
                visited[(dx,dy)] = 1
                #print(dx,dy,cost_map,visited)
                #if cost < cost_map[dy][dx]:
                cost_map[dy][dx] = cost
                queue.appendleft([dx,dy])
                xx,yy = dir[grid[dy][dx]-1]
                dx+=xx
                dy+=yy
                #print("dx",dx,"dy",dy)

            #print(queue)
            #x, y = queue.popleft()
            cost = cost_map[y][x]
            for d in dir:
                dx, dy = x+d[0], y+d[1]
                if 0<=dx<n and 0<=dy<m and(dx,dy) not in visited:
                    if cost +1 < cost_map[dy][dx]:
                        queue.append([dx, dy])
                        cost_map[dy][dx] = cost+1
                    print("cost ",cost_map)
        return cost_map[m-1][n-1]


sol = Solution()
#print("ans",sol.minCost( grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
#print("ans",sol.minCost( grid = [[3,1,4,1],[3,2,4,2],[3,1,4,1],[1,1,4,2]]))
#print("ans",sol.minCost( grid = [[1,1,3],[3,2,2],[1,1,4]]))
#print("ans",sol.minCost( grid = [[1,2],[4,3]]))
#print("ans",sol.minCost( grid = [[2,2,2],[2,2,2]]))
#print("ans",sol.minCost( grid = [[4]]))
print("ans",sol.minCost( [[4,1,4,4,4,3,4,4,1],[2,3,1,4,1,1,4,1,4],[4,3,4,2,1,3,4,2,2]]))