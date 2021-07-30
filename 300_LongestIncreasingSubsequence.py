from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        length = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    length[i] = max(length[i],length[j]+1)

        return max(length)
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:

        length = [1]
        length[0] = nums[0]
        for i in range(1,len(nums)):
            #bin search
            l = 0
            r = len(length) -1
            while l <= r:
                m = (l + r)//2
                #print("l", l, "r", r, "m", m, length)
                if length[m] < nums[i]:
                    l = m+1
                else:
                    r = m -1

            if l >= len(length):
                length.append(nums[i])
            else:
                length[l] = nums[i]
        #print(length)
        return len(length)
nums = [10,9,2,5,3,7,101,18]
print(Solution2().lengthOfLIS(nums))
# nums = [0,1,0,3,2,3]
# print(Solution().lengthOfLIS(nums))
# nums = [7,7,7,7,7,7,7]
# print(Solution().lengthOfLIS(nums))
nums = [7,8,1,2,3,7,7,8]
print(Solution2().lengthOfLIS(nums))
