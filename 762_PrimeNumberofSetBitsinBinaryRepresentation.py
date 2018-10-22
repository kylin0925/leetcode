class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isPrime(n):
            #print("chk",n)
            if n == 1:
                return False
            if n == 2:
                return True
            if n %2 ==0:
                return False
            i = 3
            while i*i <= n:
                if n % i ==0:
                    return False
                i+=1
            return True
        count = 0
        for i in range(L,R+1):
            bintext = bin(i)
            #print(bintext)
            count +=isPrime(bintext.count("1"))
        return count
sol = Solution()
test_data = [ [6,10], [10,15],[1,10001],[1,1],[2,2],[3,3],[4,4],[13,13]]
for d in test_data:
    print(sol.countPrimeSetBits(d[0],d[1]))