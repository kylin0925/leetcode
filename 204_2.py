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
        prime_table = [ 1 for i in range(n)]
        for i in range(2,n):
            #if i %1000 == 0:
            #print "start",i
            if prime_table[i] == 0:
                continue
            j=i*i    
            while j < n:
                prime_table[j] = 0
                #print "mark",j
                j += i
            '''        
            for j in range(1,n):
                if  i*i *j < n:
                    prime_table[i*i * j] = 0
                else:
                    break
            '''
        #print prime_table 
        cnt = 0
        for i in xrange(2,n):
            if prime_table [i] == 1:
                cnt+=1
        return cnt        
sol = Solution()
#test_data = [10]
test_data = [100]

for d in test_data:
    print sol.countPrimes(d)
