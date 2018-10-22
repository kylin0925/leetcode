class Solution1:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        leftp = ["(" for i in range(n)]
        rightp = [")" for i in range(n)]

        #print(leftp,rightp)

        def swap(a,i,b,j):
            tmp = b[j]
            b[j] = a[i]
            a[i] = tmp

        res = ["".join(leftp) + "".join(rightp)]
        for i in range(n-1):
            for j in range(n-1):
                print(n-i-1,j)
                # tmp = leftp[n-i-1]
                # leftp[n-i-1] = rightp[j]
                # rightp[j] = tmp

                swap(leftp,n-i-1,rightp,j)

                tmp = "".join(leftp) + "".join(rightp)
                #print(tmp)
                res.append(tmp)
                swap(leftp, n - i - 1, rightp, j)

        return res

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        data = []
        def verify(text):
            stack = []
            for c in text:
                if c == "(":
                    stack.append(c)
                else:
                    if len(stack) > 0 and stack[-1] == "(":
                        stack.pop(len(stack)-1)
                    else:
                        return False
            return True if len(stack) == 0 else False
        def dfs(lv,n,data,p):
            ps = ["(",")"]
            #print(lv,n)
            if lv == (n-1)*2:
                #print("data",data)
                if data.count("(") == data.count(")"):
                    tmp = "(" + "".join(data) + ")"
                    if verify(tmp):
                        res.append(tmp)
                return

            tmp = "("
            data.append("(")

            dfs(lv+1,n,data,tmp)
            tmp = ")"
            data[-1] = tmp
            dfs(lv + 1, n, data, tmp)
            data.pop(lv)
        dfs(0,n,data,"(")
        #print(res,len(res))
        return res

sol = Solution()
test_data = [4,3,2]
for d in test_data:
    print(sol.generateParenthesis(d))