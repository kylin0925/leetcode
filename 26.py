class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        i = 0
        if nums_len == 0:
            return 0
        for j in range(1,nums_len):   
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        i+=1        
        return i       
sol = Solution()
test_data = [[],[0,0,1,2,2],[0,0,1,2,2,3,3,3,3,3],[0,0,0,0],[0] ]
for d in test_data:
    print d
    print sol.removeDuplicates(d)
