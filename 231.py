class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """  
        if n <= 0:
            return False
        cnt = 0
        while n>0:
            #print n
            if n & 1 > 0:
                cnt+=1
            if cnt > 1:
                return False
            n = n >>1    
        return True
sol = Solution()
test_data = [0,1,2,3,4,5,6,7,100, 256 ]
for d in test_data:
    print sol.isPowerOfTwo(d)
