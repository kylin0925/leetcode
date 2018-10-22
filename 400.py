class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        digit_len = 1
        d = 9
        while n > d * digit_len:
            n -=d * digit_len
            start *=10
            digit_len+=1
            d *=10
        #print n,start,d ,digit_len
        num= ((n-1)/digit_len) + start
        return int(str(num)[(n-1)%digit_len])
sol = Solution()
test_data = [ 10,11,12,13,187,189,190,2890]
for d in test_data:
    print sol.findNthDigit(d)
