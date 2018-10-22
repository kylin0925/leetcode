class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """  
        pig = 0
        r = minutesToTest/minutesToDie +1
        
        while r**pig < buckets:
            pig+=1
        return pig
sol = Solution()
test_data = [[1,1,1], [1000,12,60] ]
for d in test_data:
    print sol.poorPigs(d[0],d[1],d[2])
