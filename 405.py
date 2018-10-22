class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        MAX_INT = 0xffffffff
        table = "0123456789abcdef"
        res = ""
        if num < 0:
            num = MAX_INT + num +1
        while num > 0:
            tmp = num %16
            res +=table[tmp]
            num /=16
        return res[::-1]
sol = Solution()
test_data = [ 64,100,-1,-3,0]
for d in test_data:
    print sol.toHex(d)
