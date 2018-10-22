class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """  
        for i in xrange(len(nums)):
            tmp = abs(nums[i]) -1
            if nums[tmp] > 0:
                nums[tmp] = -nums[tmp]
            #print nums
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
sol = Solution()
test_data = [[1],[1,1],[4,3,2,7,8,2,3,1] ]
for d in test_data:
    print sol.findDisappearedNumbers(d)
