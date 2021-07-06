from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]

        large = nums[0]
        small = nums[0]
        tmp = nums[0]
        for i in range(1,len(nums)):
            tmpsmall = small*nums[i]
            tmplarge= large*nums[i]

            small = min(nums[i],min(tmpsmall,tmplarge))
            large = max(nums[i],max(tmpsmall,tmplarge))
            maxprod = max(nums[i],max(maxprod,large))

            print(small,large,maxprod)
        return maxprod

print(Solution().maxProduct(nums = [2,3,-2,4]))
print(Solution().maxProduct(nums = [2,-3,-2,4]))
print(Solution().maxProduct(nums = [-3,0,-4]))
print(Solution().maxProduct(nums = [-3,1,1,-4,-1,10,10]))
