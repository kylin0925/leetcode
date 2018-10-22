class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        tmp = [str(c) for c in nums]
        tmp = "".join(tmp).split('0')
        maxbinlen = 0
        for b in tmp:
            if maxbinlen < len(b):
                maxbinlen = len(b)
        return maxbinlen
sol = Solution()
test_data = [ [1,1,0,1,1,1]]
for d in test_data:
    print sol.findMaxConsecutiveOnes(d)
