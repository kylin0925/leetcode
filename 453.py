class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        m = min(nums)
        res = 0
        for n in nums:
            res += n-m
        return res    
sol = Solution()
test_data = [ [1,2,3],[1],[1,3,57],[2,4,7]]
for d in test_data:
    print sol.minMoves(d)
