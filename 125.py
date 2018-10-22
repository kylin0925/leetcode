class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """  
        p = s.lower()
        pal = ""
        isPal = True
        for c in p:
            if c.isalpha() or c.isdigit():
                pal+=c
        #print pal
        
        pal_len = len(pal)
        for i in xrange(pal_len/2):
            if pal[i] != pal[pal_len -1 -i]:
                isPal = False
                break
        return isPal   
sol = Solution()
test_data = ["A man, a plan, a canal: Panama","a" ,"ab","aba","aabb","abba","0P"]
for d in test_data:
    print sol.isPalindrome(d)
