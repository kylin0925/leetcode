class Solution(object):
    def isPrime(self,n):
       
        t = 2
        if n %2 ==0:
            return False
        while t*t <= n:
            #print n,t
            if n % t == 0:
                #print "isPrime",n,"False"              
                return False
            t+=1
        
        #print "isPrime",n,"True"              
        return True    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        if n <= 1:
            return 0
        if n ==2:
            return 0
        cnt = 1
        for i in range(3,n,2):
            #print i
            if self.isPrime(i):
                cnt+=1
        return cnt        
sol = Solution()
test_data = [3,10]
for d in test_data:
    print sol.countPrimes(d)
