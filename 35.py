class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        #print nums,target
        nums_len = len(nums)
        while i < nums_len:
            #print i,nums[i]<target
            if nums[i]<target:
                i+=1
            else:
                break
        #print "res",i        
        return i
sol = Solution()
test_data = [ [[1,3,5,6], 0],[[1,3,5,6], 5],[[1,3,5,6], 2] ]
for d in test_data:
    print sol.searchInsert(d[0],d[1])
