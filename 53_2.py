class Solution(object):        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """               
        nums_len = len(nums)
        if nums_len == 0:
            return []
            
        dp = [0 for x in xrange(nums_len)]    
        max_sum = nums[0]
        dp[0] = nums[0]
        for i in range(1,nums_len):
            tmp =0
            if dp[i-1] > 0:
                tmp = dp[i-1]
            dp[i] = nums[i] + tmp
            if dp[i] >max_sum:
               max_sum = dp[i]
                
        return max_sum
sol = Solution()
test_data = [ [-2,1,-3,4,-1,2,1,-5,4],[1,2,7],[-1,-1,1,9],[],[1],[0,0],[-1,-1],[-2,1]]
#test_data = [ [1,2]]
for d in test_data:
    print sol.maxSubArray(d)
