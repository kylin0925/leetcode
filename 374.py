# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
Tar = 99
def guess(num):
    print "guess",num,num>Tar
    if num > Tar:
        return -1
    if num == Tar:
        return 0
    if num < Tar:
        return 1    
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        g = int(((start +end)/2.0 +.5))
       
        while start<=end:              
            r = guess(g)
            #print start,end,r
            if r ==-1:
                end = g-1
                g = int(((start +end)/2.0 +.5))           
            elif r == 1:                 
                start = g+1
                g = int(((start +end)/2.0 +.5))              
            else:
                return g
              
sol = Solution()
test_data = [ 100]
for d in test_data:
    print sol.guessNumber(d)
