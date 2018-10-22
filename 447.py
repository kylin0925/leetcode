class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        num_points = len(points) 
        #print num_points
        res =0
        for i in xrange(num_points):
            table = {}
            for j in xrange(num_points):
                if i == j:
                    continue
                dx = (points[i][0] -  points[j][0])
                dx = dx*dx
                dy = (points[i][1] -  points[j][1])
                dy = dy * dy
                d = dx+dy
                if table.has_key(d):
                    table[d] = table[d]+1
                else:
                    table[d] = 1
                  
            for k in table.itervalues():
                res += k * (k-1)
        return res        
sol = Solution()
test_data = [ [[0,0],[1,0],[2,0]] ]
for d in test_data:
    print sol.numberOfBoomerangs(d)
