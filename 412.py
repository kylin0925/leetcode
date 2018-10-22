class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """ 
        res = []
        for i in xrange(1,n+1):
            if i % 15 ==0:
                res.append("FizzBuzz")
            elif i %3 == 0:
                res.append("Fizz")
            elif i %5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res        
sol = Solution()
test_data = [15]
for d in test_data:
    print sol.fizzBuzz(d)
