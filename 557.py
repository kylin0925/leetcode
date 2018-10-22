class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """  
        lst = s.split()
        res = ""
        for w in lst:
            res+=w[::-1] + " "
        return res.strip()    
sol = Solution()
test_data = [ "Let's take LeetCode contest"]
for d in test_data:
    print sol.reverseWords(d)
