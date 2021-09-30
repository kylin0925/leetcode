class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(0,len(points)-1):
            dx = abs(points[i+1][0] - points[i][0])
            dy = abs(points[i+1][1] - points[i][1])
           
            ans+=  max(dx,dy) # diag+straight -> min(dx, dy) + [max(dx, dy) - min(dx, dy)] = max(dx, dy) 
        return ans
