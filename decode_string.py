class Solution:
    def decodeString(self, s: str) -> str:
        org_stack = []
        res = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                d = ""
                while i < len(s) and s[i].isdigit():
                    d += s[i]
                    i += 1
                org_stack.append(int(d))
            elif s[i].isalpha():
                tmp = ""
                while i < len(s) and s[i].isalpha():
                    tmp += s[i]
                    i += 1
                org_stack.append(tmp)
            else:
                org_stack.append(s[i])
                i += 1
        def dfs(i,stack):
            #if str , cat to res
            # if number , number [dfs(i)]
            res = ""
            while i < len(stack):
                if type(stack[i]) == str and stack[i]!= '[' and stack[i]!=']':
                    res +=stack[i]
                    i+=1
                elif type(stack[i]) == int:
                    r = stack[i]
                    i,tmp = dfs(i+2, stack)
                    res += tmp*r
                elif stack[i] == "]":
                    i+=1
                    break

            return i,res

        print("tmp", org_stack)
        res = ""
        i = 0
        while i < len(org_stack):
            if type(org_stack[i]) == str:
                res+= org_stack[i]
                i += 1
            else:
                i,tmp = dfs(i,org_stack)
                res+=tmp

        return res

s = Solution()
print(s.decodeString("3[a2[bc]]zz"))