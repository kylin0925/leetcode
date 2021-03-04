from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def verify(n, weights, d, numw):

            i = 0
            while d > 0:
                tmp = 0
                while i < numw:

                    w = tmp + weights[i]
                    if w > n:
                        break
                    tmp = w
                    i += 1
                if i == numw:
                    break
                d -= 1
            # print(i)
            return i == numw

        lb = 0
        ub = sum(weights)
        numw = len(weights)
        while (ub - lb) > 1:
            mid = (lb + ub) // 2
            # print(lb, mid, ub)
            if verify(mid, weights, D, numw) == True:
                ub = mid
            else:
                lb = mid

        return lb + 1

sol = Solution()
print("ans",sol.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], D = 5) == 15)
print("ans",sol.shipWithinDays(weights = [3,2,2,4,1,4], D = 3) == 6)
print("ans",sol.shipWithinDays(weights = [1,2,3,1,1], D = 4) == 3)

[1,6,2,7,3,8,4,9,5,10]