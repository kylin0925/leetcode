from typing import List


# class Solution:
#     def eatenApples(self, apples: List[int], days: List[int]) -> int:
#         dayslen = len(days)
#
#         maxdays = 0
#         for i in range(dayslen):
#             if maxdays < i + days[i]:
#                 maxdays = i + days[i]
#         maxdays += 1
#         rotmap = [0 for i in range(maxdays)]
#
#         for i in range(dayslen):
#             rotmap[i + days[i]] += apples[i]
#         print(rotmap)
#         d = 0
#         r = 0
#         for i in range(maxdays):
#             r -= rotmap[i]
#             r = 0 if r < 0 else r
#             if i < dayslen:
#                 r += apples[i] - 1
#             else:
#                 r -= 1
#
#             if r >= 0:
#                 d += 1
#
#         return d
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        n = len(apples)
        rotdays = [days[i]+i for i in range(n)]
        print(rotdays)
        m = []
        d=0
        i=0
        while i < n:
            heapq.heappush(m,[rotdays[i],apples[i]])
            j = 0
            h = []
            qsize = len(m)
            while j < qsize:
                h = heapq.heappop(m)
                if h[0] > i and h[1]>0:
                    break
                j+=1

            if h[1] > 0 and h[0]>i:
                h[1]-=1
                d+=1
                heapq.heappush(m,h)
            i+=1

        while len(m)>0:
            qsize = len(m)
            h=[]
            j=0
            while j < qsize:
                h = heapq.heappop(m)
                if h[0] > i and h[1] > 0:
                    break
                j += 1
            if len(h) == 0:
                continue
            if h[1] > 0 and h[0]>i:
                h[1]-=1
                d+=1
                heapq.heappush(m,h)
            i+=1
        return d
print(Solution().eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2]))
print(Solution().eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]))
print(Solution().eatenApples(apples = [2,1,10], days = [2,10,1]))
print(Solution().eatenApples(apples = [2,1,1,4,5], days = [10,10,6,4,2]))


