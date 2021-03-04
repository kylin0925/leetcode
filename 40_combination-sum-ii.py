from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        target_map = {}
        lenlist = len(candidates)
        res = []
        ret_res = []
        candidates.sort()
        _target = target

        def dfs(candidates, idx, n):

            if n == _target:
                tmp = ",".join(str(x) for x in res)
                if target_map.get(tmp) == None:
                    target_map[tmp] = 1
                    ret_res.append(res[:])
                    #print(ret_res)

            if n > _target:
                return
            for i in range(idx, lenlist):
                res.append(candidates[i])
                dfs(candidates, i + 1, n + candidates[i])
                del res[-1]

        dfs(candidates, 0, 0)
        #print(ret_res)
        return ret_res

sol = Solution()
ans = sol.combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],27)
print(ans)