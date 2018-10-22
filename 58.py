class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        res = s.split()
        if len(res) == 0:
            return 0
        return len(res[-1])    
sol = Solution()
test_data = [ "","Hello World","hello","a bdd c","abc, ddef, alaal" ]
for d in test_data:
    print sol.lengthOfLastWord(d)
