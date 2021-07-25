import time
# class Solution:
#     tbl = []
#     def numSquares(self, n: int) -> int:
#         start = time.time()
#         maxsq = int(n**0.5)
#         tbl = [[0 for i in range(n+1)] for j in range(maxsq+1)]
#         tbl[1] = [i for i in range(n+1)]
#         print("arr init",time.time() - start)
#         for p in range(2,maxsq+1):
#             p2 = p**2
#             for i in range(1, n+1):
#                 if i < p2:
#                     tbl[p][i] = tbl[p-1][i]
#                 else:
#                     r = i - p2
#                     c = tbl[p][r] + 1
#                     tbl[p][i] = min(c, tbl[p-1][i])
#         #print(tbl)
#         return tbl[maxsq][n]
class Solution:
    tbl = [0]
    def numSquares(self, n: int) -> int:
        for i in range(1, n+1):
            p2 = 1
            tmp =i
            while p2*p2 <= i:
                r = i - p2*p2
                tmp = min(self.tbl[r] + 1,tmp)
                p2+=1

            self.tbl.append(tmp)
        #print(self.tbl)
        return self.tbl[n]

print(Solution().numSquares(12))
print(Solution().numSquares(16))
# print(Solution().numSquares(21))
# print(Solution().numSquares(999))

start = time.time()
print(Solution().numSquares(10000))
print(time.time() - start)
# print(Solution().numSquares(1234))

