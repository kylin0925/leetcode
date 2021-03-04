from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        n = len(apples)
        m = []
        d = 0
        i = 0
        while i < n or len(m) > 0:
            if i < n :
                heapq.heappush(m, [i + days[i], apples[i]])
            if len(m) > 0:
                h = [0, 0]
                while len(m):
                    h = heapq.heappop(m)
                    if len(h) > 0 and h[1] > 0 and h[0] > i:
                        break
                if len(h) > 0 and h[1] > 0 and h[0] > i:
                    h[1] -= 1
                    d += 1
                    heapq.heappush(m, h)

            i += 1
        return d
print(Solution().eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2]))
print(Solution().eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]))
print(Solution().eatenApples(apples = [2,1,10], days = [2,10,1]))
print(Solution().eatenApples(apples = [2,1,1,4,5], days = [10,10,6,4,2]))
print(Solution().eatenApples(apples = [20000], days = [20000]))


