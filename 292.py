class Solution(object):
   def canWinNim(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n % 4 == 0:
        return False
    else:
        return True
sol = Solution()
test_data = [ 1,2,3,4,5,6,7,8,9,10]
for d in test_data:
    print sol.canWinNim(d)
