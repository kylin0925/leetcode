class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""

        while n != 0:
            p = (n -1) % 26
            #print "debug",p
            res += chr(p+ord('A'))
            n = (n-1)/26
        
        return res[::-1]
sol = Solution()
test_data = [1,26,28,702,701]
for d in test_data:
    print sol.convertToTitle(d)
