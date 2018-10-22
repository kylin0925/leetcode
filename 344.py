class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]   
sol = Solution()
test_data = ["hello","world" ]
for d in test_data:
    print sol.reverseString(d)
