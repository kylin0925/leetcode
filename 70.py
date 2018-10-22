class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2    
        idx = 3
        res = 0
        while idx <=n:
            res = a + b
            a = b
            b = res
            idx+=1
        return res    
sol = Solution()
test_data = [4,5,6,7,8,9,10 ]
for d in test_data:
    print sol.climbStairs(d)
