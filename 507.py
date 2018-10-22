class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        res = 1
        i=2
        while i* i<=num:
            if num % i == 0:
                res += i + num/i
                #print res
            i+=1    
        #print res        
        return res == num        
sol = Solution()
test_data = [ 28,24036583,20996011]
for d in test_data:
    print sol.checkPerfectNumber(d)
