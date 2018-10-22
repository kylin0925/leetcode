class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """   
        k = k % len(nums)
        tmp = nums
        tmp = tmp[-k:] + tmp[0:-k]
        
        
        for i in xrange(len(tmp)):
            nums[i] = tmp[i]
        print nums
sol = Solution()
test_data = [ [[1,2,3,4,5,6,7] ,3] ]
for d in test_data:
    sol.rotate(d[0],d[1])
    print d[0]
