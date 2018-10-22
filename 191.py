class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            b = (n & 1) > 0
            cnt += b
            n = n >>1
        return cnt    
sol = Solution()
test_data = [11,128 ,100]
for d in test_data:
    print sol.hammingWeight(d)
