class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """ 
        if num == 0:
            return "0"
        sign = 1
        if num < 0:
            sign = -1
            num = -num
        res = ""    
        while num > 0:
            res += str(num % 7)
            num/=7
        res = res[::-1]
        if sign ==-1:
            res = "-"+res
        
        return res
sol = Solution()
test_data = [100,7,-7 ,0,-1,1,5]
for d in test_data:
    print sol.convertToBase7(d)
