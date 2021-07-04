from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = [-1 for i in range(len(s)) ]

        def dfs(i, catstr):

            if catstr == s:
                return True
            if i > len(s):
                return False
            r=False
            if memo[i]!=-1:
                return memo[i]

            for w in wordDict:
                if s[i:len(w) + i] == w:
                    r |= dfs(i + len(w), catstr + w)

            memo[i] = r
            return r

        ans = dfs(0,"")

        return ans

print(Solution().wordBreak( s = "leetcode", wordDict = ["leet","code"]))
print(Solution().wordBreak( s = "applepenapple", wordDict = ["apple","pen"]))
print(Solution().wordBreak( s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
print(Solution().wordBreak( s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc", wordDict = ["g","dog","c","a","t","ab","abc","s"]))
