from typing import List

class Solution:
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

print(Solution().partition(s = "aab"))
print(Solution().partition(s = "a"))
print(Solution().partition(s = "aaaaaaaaaaaaaaaa"))
