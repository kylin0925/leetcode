class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        table = [1,3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969,14348907,
                43046721,129140163,387420489,1162261467,3486784401,10460353203,31381059609,94143178827]
        #import math
        #if n < 0:
        #    return False
        #if n == 0:
        #    return False
        #if n ==1:
        #    return True
        #p = math.log(n)/math.log(3)
        
        #print p%1
        return  n in table
sol = Solution()
test_data = [0, 1,2,3,4,5,6,7,8,9,10,21,22,23,27,64,81,19682,243]
for d in test_data:
    print sol.isPowerOfThree(d)
#0.00000000000001