class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A = s.count('A')
        L = s.count('LLL')
        return A<=1 and L<1
sol = Solution()
test_data = ["PPALLP",  "PPALLL","LALL"]
for d in test_data:
    print sol.checkRecord(d)
