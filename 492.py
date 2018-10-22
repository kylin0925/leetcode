class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        r = area**0.5
        l = int(r + 0.5)        
        w = int(r)
        while w > 0:
            if area % w ==0:             
                return [area/w,w]
            w-=1    
sol = Solution()
test_data = [4 ,9,14,101,63,110]
for d in test_data:
    print sol.constructRectangle(d)
