class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_pos = 2147483647L
        min_pos = -2147483648L
        s = str(x)
        ans = ""
        if x >=0:
            ans = s[::-1]
        else:
            ans = s[::-1]
            ans = ans[0:-1]
            ans = "-"+ans
        a = int(ans)
        if a > max_pos:
            a = 0
        elif a < min_pos:
            a=0
        return a
a = Solution()

n = a.reverse(3)
print n == 3
n = a.reverse(1534236469)
print n == 0

n = a.reverse(-23)
print n == -32
