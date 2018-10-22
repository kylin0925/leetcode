class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """ 
        i=1
        while num > 0:
            num -=i
            i+=2
        return num == 0
sol = Solution()
test_data = [ 1,4,9,16,77,88,121]
for d in test_data:
    print sol.isPerfectSquare(d)
