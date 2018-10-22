class Solution(object):
    def myAtoi(self, x):
        """
        :type x: int
        :rtype: int
        """
        if len(x)==0:
            return 0
        max_pos = 2147483647L
        min_pos = -2147483648L
        try:
            ans = int(x)
        except:
            ans = 0
        if ans > max_pos or ans < min_pos:
            ans = 0
         
        return ans
a = Solution()

n = a.myAtoi("+")
print n == 0
n = a.myAtoi("3")
print n == 3
n = a.myAtoi("2221534236469")
print n == 0

n = a.myAtoi("-23")
print n == -23

n = a.myAtoi("+23")
print n == -23
