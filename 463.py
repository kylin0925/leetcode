class Solution(object):
    def nebor(self,grid,x,y):
        cnt = 0
        if y > 0:
            if grid[y-1][x] == 1:
                cnt+=1
        if y < len(grid) -1:
            if grid[y+1][x] == 1:
                cnt+=1
        if x > 0:
            if grid[y][x-1] == 1:
                cnt+=1
        if x < len(grid[0]) -1:
            if grid[y][x+1] == 1:
                cnt+=1
        return cnt        
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        y = len(grid)
        x = len(grid[0])
        p =0
        for i in xrange(y):
            for j in xrange(x):
                if(grid[i][j]==1):
                    p += 4-self.nebor(grid,j,i)
        return p    
sol = Solution()
test_data = [ []
[[0,1,0,0],
 [1,1,1,0],
 [0,0,0,0],
 [0,0,0,0]]]
for d in test_data:
    print sol.islandPerimeter(d)
