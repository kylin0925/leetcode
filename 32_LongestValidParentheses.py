class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lens = len(s)
        dp = [0 for x in range(lens)]
        stack = []
        max_len = 0
        for i in range(lens):
            if s[i] == '(':
                stack.append(i)

            else:
                if len(stack) > 0:
                    idx = stack[-1]
                    dp[idx] = 1
                    dp[i] = 1


                    stack.pop()
            #print(dp)

        #print(max_len)
        cnt = 0
        for i in range(lens):
            if dp[i] ==1:
                cnt+=1
            else:
                if max_len < cnt:
                    max_len=cnt
                cnt=0
        if max_len < cnt:
            max_len=cnt
        return max_len

sol = Solution()
print(sol.longestValidParentheses(")(())()"))
print(sol.longestValidParentheses(")(()())"))
print(sol.longestValidParentheses(")"))
print(sol.longestValidParentheses(""))
print(sol.longestValidParentheses("()"))
print(sol.longestValidParentheses("())"))
print(sol.longestValidParentheses(")()())"))
print(sol.longestValidParentheses("))())"))
print(sol.longestValidParentheses("()(())"))
print(sol.longestValidParentheses("()(()"))
print(sol.longestValidParentheses("()(()((()()()"))
