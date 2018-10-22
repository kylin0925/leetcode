class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fn = (1 + n ) * n / 2
        if n <= 0:
            return 0
        if n == 1:
            return 1
        idx = 0
        i=1
        #print "n",n
        while i <=n:
            fn = (1 + i ) * (i)/2
            #print i,"fn",fn
            if fn > n:
                idx = i -1
                #print i,idx
                break
            i+=1    
        return idx
sol = Solution()
test_data = [2,3,4,5,8]
for d in test_data:
    print sol.arrangeCoins(d)
