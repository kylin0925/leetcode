from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(s):
            #print(s)
            ans = []
            for i,c in enumerate(s):
                if c in "+-*/":
                    r = dfs(s[i+1:])
                    l = dfs(s[0:i])
                    #print("l",l,"r",r,c)
                    for i in l:
                        for j in r:
                            ans.append(eval(str(i)+c+str(j)))
            return ans if len(ans) > 0 else [int(s)]
        ans = dfs(expression)
        return ans


print(Solution().diffWaysToCompute(expression = "2*3-4*5"))
print(Solution().diffWaysToCompute(expression = "2*3-4*5*5*5*5*5*5*55"))