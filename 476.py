class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """ 
        n = num
        cnt = 0
        while n > 0:
            cnt+=1
            n>>=1
        return 2**cnt -1 - num    
sol = Solution()
test_data = [5,0, 8,11]
for d in test_data:
    print sol.findComplement(d)
