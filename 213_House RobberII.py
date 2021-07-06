from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def maxrob(l,r,nums):
            if len(nums) == 1:
                return nums[0]
            dp = [0 for i in range(len(nums))]
            dp[l] = nums[l]
            dp[l+1] = max(nums[l], nums[l+1])

            for i in range(l+2,r):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            #print(dp)
            return dp[r-1]
        a = maxrob(0,len(nums)-1, nums)
        b = maxrob(1,len(nums), nums)
        #print(a,b)
        return max(a, b)

# print(Solution().rob(nums = [1,2,3,1]))
# print(Solution().rob(nums =  [2,3,2]))
# print(Solution().rob(nums =  [2]))
print(Solution().rob(nums =  [10,2,10,0,1]))
print(Solution().rob(nums =  [200,3,140,20,10]))