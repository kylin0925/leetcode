# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         s_len = len(s)
#         p_len = len(p)
#         self.level = 0
#
#         def match(i, j, s, p):
#             #print(self.level,i,j)
#             if p[j:] == '*':
#                 return True
#             while i < s_len or j < p_len:
#                 if i< s_len and j<p_len and p[j]!='*' and (p[j] == s[i] or p[j] == '?'):
#                     i+=1
#                     j+=1
#                 elif j<p_len and p[j] == "*":
#                     if j == p_len -1:
#                         return True
#                     while j < p_len:
#                         if p[j] == '*':
#                             j+=1
#                         else:
#                             break
#                     j-=1
#                     for t in range(s_len+1):
#                         self.level+=1
#                         r = match(i + t, j + 1, s, p)
#                         self.level-=1
#                         if r:
#                             return r
#                     return False
#                 else:
#                     break
#
#             return j == p_len and i == s_len
#
#         return match(0, 0, s, p)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        dp = [ [False for j in range(p_len+1)] for i in range(s_len+1)]
        dp[0][0] = True
        for i in range(1,p_len+1):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break
        #print(dp[0])
        for i in range(1,s_len+1):
            for j in range(1,p_len+1):
                if p[j-1]!= '*':
                    dp[i][j] = dp[i - 1][j - 1] and (p[j-1] == s[i-1] or p[j-1] == "?")
                else:
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[s_len][p_len]



sol = Solution()
print(sol.isMatch("abc","abc**"))
print(sol.isMatch("aad","aa?"))
print(sol.isMatch("a","a*"))
print(sol.isMatch("ab","*"))
print(sol.isMatch("","*"))
print(sol.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab","***bba**a*bbba**aab**b"))
print(sol.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab","*bba*a*bbba*aab*b"))
print(sol.isMatch("abcdefghijk","*****k***a"))
print(sol.isMatch("babbbaabbaaaaabbababaaaabbbbbbbbbbabbaaaabbababbabaa", "**a****a**b***ab***a*bab"))