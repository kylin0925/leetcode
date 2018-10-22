class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        h = x ^ y
        cnt = 0
        while h > 0:
            cnt += h & 1
            h >>=1
        return cnt    
sol = Solution()
test_data = [[1,4],[0,1],[0,3],[1,12] ]
for d in test_data:
    print sol.hammingDistance(d[0],d[1])
