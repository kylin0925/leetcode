from typing import List

class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.tmp = []

        def check(s):
            #print(s)
            mid = len(s)>>1
            l = len(s)
            for i in range(0,mid):
                if s[i]!=s[l-i-1]:
                    return False
            return True
        def dfs(i):
            if i == len(s):
                self.ans.append(self.tmp[:])
                #print(self.tmp,self.ans)
                return
            for j in range(1,len(s)+1):
                if j+i <= len(s) and check(s[i:j+i]):
                    self.tmp.append(s[i:j+i])
                    dfs(j+i)
                    self.tmp.pop()
        dfs(0)
        return self.ans
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = [ [] for i in range(len(s))]
        self.tmp = []

        def check(s):
            #print(s)
            mid = len(s)>>1
            l = len(s)
            for i in range(0,mid):
                if s[i]!=s[l-i-1]:
                    return False
            return True

        def dfs(i):
            if i == len(s):
                #self.ans.append(self.tmp[:])
                #print(self.tmp,self.ans)
                return [[]]
            tmp = []
            if len(self.ans[i]) > 0 :
                #print("get cache")
                return self.ans[i]
            for j in range(1,len(s)+1):
                p = s[i:j+i]
                if j+i <= len(s) and check(p):
                    subans = dfs(j+i)
                    for r in subans:
                            tmp.append([p] + r)
            self.ans[i] = tmp
            return tmp
        dfs(0)
        #print(self.ans)
        return self.ans[0]
import time
start = time.time()
#print(Solution().partition(s = "aab"))
#print(Solution().partition(s = "a"))

print(Solution().partition(s = "aaaaaaaaaaaaaaaa") == Solution2().partition(s = "aaaaaaaaaaaaaaaa"))
print(Solution().partition(s = "abceecba") == Solution2().partition(s = "abceecba"))
#print(Solution().partition(s = "aaaa"))
print(time.time() - start)

