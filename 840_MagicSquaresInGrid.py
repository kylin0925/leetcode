class Solution(object):
    # a b c 
    # d e f
    # g h i 
    def checkMagic(self,a,b,c,d,e,f,g,h,i):
        #print a,b,c,d,e,f,g,h,i
        table = [a,b,c,d,e,f,g,h,i]
        table.sort()
        all_sum = sum(table)
        #print all_sum
        return table == range(1,10) and a + b + c == d+e+f == g+h+i and a + d + g == b + e + h == c + f + i and a + e + i == c + e + g
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 
        grid_h = len(grid)
        grid_w = len(grid[0])
        cnt = 0
        for y in range(grid_h-2):
            for x in range(grid_w-2):
                
                if self.checkMagic(grid[y  ][x],grid[y  ][x+1],grid[y][x+2],
                            grid[y+1][x],grid[y+1][x+1],grid[y+1][x+2],
                            grid[y+2][x],grid[y+2][x+1],grid[y+2][x+2],) :
                            cnt+=1
        return cnt                    
sol = Solution()
test_data = [ 
        [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]],[[10,3,5],[1,6,11],[7,9,2]] ,[[10,3,],[1,6]],[[10,3,],[1,6],[1,6]] ,[[1,8,6],[10,5,0],[4,2,9]]
        ]

for d in test_data:
    print sol.numMagicSquaresInside(d)
