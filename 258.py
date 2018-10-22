class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return 1 + (num -1 ) % 9
sol = Solution()
test_data = [38,10,99,100 ,0]
for d in test_data:
    print sol.addDigits(d)
