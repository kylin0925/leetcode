class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        c =0
        
        while(b!=0):
            #print a,b
            c = (a & b) & 0xFFFFFFFF            
            a = (a ^ b) & 0xFFFFFFFF
            b = (c <<1) & 0xFFFFFFFF
            
            #bb=raw_input()
        return a if a < 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)
sol = Solution()
test_data = [ [-1,3],[-44,-33],[456,0],[123,7],[2,8]]
for d in test_data:
    print sol.getSum(d[0],d[1])
