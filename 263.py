class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        d = 2
        while num > 1:
            #print d,num
            if num %d != 0:
                d+=1
            if d > 5:
                return False
            if num % d ==0:    
                num = num / d
            else:
                d+=1
        if num >5:
            return False
        else:
            return True    
sol = Solution()
test_data = [ 25,6,8,14,15,22,49,35,66]
for d in test_data:
    print sol.isUgly(d)
