from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        premax = 0
        premin = 0
        maxsum = 0
        minsum = 10**9+7

        for x in nums:
            premax = max(0, premax +x )
            maxsum = max(maxsum, premax)

            premin = min(0, premin + x)
            minsum = min(minsum, premin)
            #print(x,maxsum,minsum,premin)

        return max(abs(maxsum), abs(minsum))


# print(Solution().maxAbsoluteSum(nums = [1,-3,2,3,-4]) == 5)
# print(Solution().maxAbsoluteSum( nums = [2,-5,1,-4,3,-2]) == 8)
print(Solution().maxAbsoluteSum( nums = [-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9])==44)
print(Solution().maxAbsoluteSum( nums = [-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8])==27)
