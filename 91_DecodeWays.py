from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        self.num_dec = 0

        def dfs(i,s):
            #print(i)
            if i == len(s):
                self.num_dec+=1
                #print("self.num_dec ", self.num_dec )
                return
            if s[i]!= '0':
                #print("i+1")
                dfs(i+1, s)
                if i+1<len(s):
                    tmp = int(s[i:i+2])
                    if tmp <= 26:
                        #print("i+2",i)
                        dfs(i+2, s)
        dfs(0, s)
        return self.num_dec

class Solution1:
    def numDecodings(self, s: str) -> int:
        if s == "0":
            return 0
        if len(s) ==1:
            return 1

        dp = [0 for i in range(len(s))]

        if s[-1]!='0':
            dp[-1]=1
        tmp =0
        if 1<=int(s[-2:])<=26:
            tmp = 1
        if s[-2]!='0':
            dp[-2] = dp[-1]+tmp

        for i in range(len(s)-3,-1,-1):
            one = 0
            if s[i]!='0':
                one=dp[i+1]
            two = 0
            if 1<= int(s[i:i+2]) <=26 and s[i]!='0':
                two=dp[i+2]
            dp[i] = one+two
        #print(dp)
        return dp[0]
print(Solution1().numDecodings("1201234") == Solution().numDecodings("120 1 234"))
#print(Solution1().numDecodings("226") == Solution().numDecodings("226"))
#print(Solution1().numDecodings("11106") == Solution().numDecodings("11106"))
#print(Solution().numDecodings("123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789"))
# print(Solution1().numDecodings("12")==Solution().numDecodings("12"))
# print(Solution1().numDecodings("06")==Solution().numDecodings("06"))
# print(Solution1().numDecodings("111111111111111111111111111111111111111111111") == 1836311903)
# 1134903170
# 1836311903
# print(Solution1().numDecodings("1111938549034850934850") == Solution().numDecodings("1111938549034850934850"))
# print(Solution1().numDecodings("61"))
# print(Solution1().numDecodings("21"))
# print(Solution1().numDecodings("0"))
# print(Solution1().numDecodings("22222222222222") == 610)
# print(Solution1().numDecodings("1001") == 0)
#print(Solution1().numDecodings("1111"))
'''
'A' -> "1"
'B' -> "2"

'Z' -> "26"
"1" 1 
"11" 2
"111" 3
"1111" 5
"11111" 8


1
2
3
5
8
t
" 1 1 1 1 1 1 0"
  1 2 3 5 8 13
'''