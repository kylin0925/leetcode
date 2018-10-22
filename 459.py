class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = s + s 
        tmp = tmp[1:-1]
        return tmp.count(s) > 0
sol = Solution()
test_data = [ "abcabcabcabc","aba","a","aabaab"]
for d in test_data:
    print sol.repeatedSubstringPattern(d)
