class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """  
        tmp = s[::-1]
        i = 0
        r = 0
        for c in tmp:
            r += (ord(c) - ord('A') +1) * (26 ** i) 
            i+=1
            
        return r    
sol = Solution()
test_data = [ "A","AB","ZY"]
for d in test_data:
    print sol.titleToNumber(d)
