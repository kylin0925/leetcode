from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:

        idx = 0
        gidx = 0
        while idx < len(nums) and gidx<len(groups):
            glen = len(groups[gidx])
            if nums[idx:idx+glen] == groups[gidx]:
                gidx+=1
                idx+=glen
            else:
                idx+=1

        return gidx == len(groups)


print(Solution().canChoose(groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]))
print(Solution().canChoose(groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,1,2,3,3,-2,0]))
print(Solution().canChoose(groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]))
print(Solution().canChoose(groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]))