class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(i,s):
            tmps = ""
            d = ""
            while i < len(s):
                c = s[i]
                if c.isalpha():
                    tmps +=c
                elif c.isdigit():
                    d+=c
                elif c == '[':
                    ei,exps = dfs(i+1,s)
                    tmps += exps * int(d)
                    d = ""
                    i=ei
                elif c == ']':
                    return i,tmps
                i+=1
            return tmps
        res = dfs(0,s)

        return res

s = Solution()
print(s.decodeString("3[a2[bc]]zz2[bc]"))
print(s.decodeString("zz2[bb]3[cc]"))