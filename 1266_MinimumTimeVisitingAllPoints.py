class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(0,len(points)-1):
            dx = abs(points[i][0] - points[i+1][0])
            dy = abs(points[i][1] - points[i+1][1])
            #print(dx,dy)
            if dx == dy:
                ans+=dx
            elif dx==0 or dy ==0:
                ans+=dx+dy
            else:
                d = min(dx,dy)
                newx = 0
                newy = 0
                if points[i][0] < points[i+1][0]:
                    newx = points[i][0]+d
                else:
                    newx = points[i][0]-d
                    
                if points[i][1] < points[i+1][1]:
                    newy = points[i][1]+d
                else:
                    newy = points[i][1]-d
                    
                dx = abs(points[i+1][0] - newx)
                dy = abs(points[i+1][1] - newy)
                ans+=d +dx+dy
                #print(ans)  
        return ans
        
        
        
# go diag (x,y)
# a b -> diag can reach
# a b -> h 
# a b -> v
# a b -> go diag then h


