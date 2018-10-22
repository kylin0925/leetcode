class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt_5 = 0
        
        while n > 0:
            cnt_5 += n/5
            n=n/5
        return cnt_5
sol = Solution()
test_data = [1,5,10,25,100 ]
for d in test_data:
    print sol.trailingZeroes(d)
    
    
    
#000000000000000000000000L