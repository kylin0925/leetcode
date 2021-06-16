from typing import List
from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        @lru_cache(2000)
        def dfs(l,r,i):
            if i == m :
                return 0
            lval = nums[l]*multipliers[i] + dfs(l+1,r,i+1)
            rval = nums[r]*multipliers[i] + dfs(l,r-1,i+1)
            return max(lval,rval)


        return dfs(0,n-1,0)

#print(Solution().maximumScore(nums = [1,-2,3], multipliers = [1,2,-3]))
#print(Solution().maximumScore(nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]))
#m = [x for x in range(200)]
#nums = [x for x in range(1000)]
#print(len(m))
nums = [-947,897,328,-467,14,-918,-858,-701,-518,-997,22,259,-4,968,947,582,-449,895,-121,-403,633,490,64,543,-396,-997,841,-398,247,297,-147,-708,804,-199,-765,-547,-599,406,-223,-11,663,746,-365,-859,256,-25,919,-334,490,-511,865,-139,-968,961,-793,451,317,645,-294,240,-312,-822,961,-572,309,579,161,780,525,-622,-511,423,946,-28,-199,822,-123,-316,-913,113,-458,-428,-414,49,922,722,-854,323,-219,581,302,124,164,31,727,186,308,-936,-937,-862,939,213,966,-74,-76,-1,521,777,-966,454,-199,526,-895,447,-749,-518,-639,849,-771,979,-760,-763,-601,-201,40,-911,207,890,-942,-352,700,267,830,-396,536,877,-896,-687,262,-60,-373,-373,526]
m = [864,849,586,769,309,-413,318,652,883,-690,796,251,-648,433,1000,-969,422,194,-785,-242,-118,69,187,-925,-418,-556,88,-399,-619,-383,-188,206,-793,-9,738,-587,878,360,640,318,-399,-366,365,-291,-75,-451,-674,-199,177,862,1,11,390,-52,-101,127,-354,-717,-717,180,655,817,-898,28,-641,-35,-563,-737,283,-223,-322,-59,955,172,230,512,-205,-180,899,169,-663,-253,270,651,168,417,613,-443,980,-189,417,372,-891,-272,993,-877,906,680,-630,-328,-873,-811,78,-667,-2,190,-773,878,529,620,-951,-687,314,-989,-48,-601,-950,31,-789,-663,-480,750,-872,-358,529,-426,-111,517,750,-536,-673,370]
print(Solution().maximumScore(nums,m))