from typing import List


# class Solution:
#     def constructDistancedSequence(self, n: int) -> List[int]:
#         self.found = False
#         self.maxlen = (n - 1) * 2 + 1
#         self.res = [0 for i in range(self.maxlen)]
#         self.found = False
#         def dfs(n):
#             if n == 0:
#                 print(self.res)
#                 #self.found =True
#                 return
#
#             for i in range(self.maxlen):
#                 if n == 1 and self.res[i] == 0:
#                     self.res[i] = n
#                     dfs(n - 1)
#                     self.res[i] = 0
#                 elif i+n < self.maxlen and self.res[i] == 0 and self.res[i+n] == 0:
#                     self.res[i] = n
#                     self.res[i + n] = n
#                     dfs(n-1)
#                     self.res[i] = 0
#                     self.res[i + n] = 0
#
#         dfs(n)
#         return self.res
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        self.maxlen = (n - 1) * 2 + 1
        self.res = [0 for i in range(self.maxlen)]
        self.found = False
        self.n = n
        self.flag = [0 for i in range(n+1)]

        def dfs(d): # d  position

            while d < self.maxlen and self.res[d]!=0 :
                d=d+1
            if d ==self.maxlen:
                #print("ans ", self.res, d, self.flag)
                self.found = True
                return

            for i in range(self.n,0,-1): # is target number
                if self.flag[i] == 1:
                    continue
                if i == 1 and self.res[d] == 0:
                    self.res[d] = i
                    self.flag[i] =1
                    dfs(d + 1)
                    if self.found:
                        return
                    self.flag[i] = 0
                    self.res[d] = 0
                elif i+ d < self.maxlen and self.res[d] == 0 and self.res[d+i] == 0:
                        self.res[d] = i
                        self.res[d + i] = i
                        self.flag[i] = 1
                        dfs(d+1)
                        if self.found:
                            return
                        self.flag[i] = 0
                        self.res[d] = 0
                        self.res[d + i] = 0

        dfs(0)
        return self.res
tbl = []
for i in range(1,21):
    tbl.append(Solution().constructDistancedSequence(i))
print(tbl)
