class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        def dfs(text):
            global  res

            #print("text",text)
            tmp = ""
            cnt = 0

            stack = []
            j=0
            for i in range(0,len(text)):
                #print(i,cnt )
                if text[i] == "1":
                    cnt+=1
                elif text[i] == "0":
                    cnt-=1
                if cnt == 0:
                    tmp = "1" + dfs(text[j+1:i]) + "0"
                    #print("tmp",tmp)
                    stack.append(tmp)
                    #print(tmp)
                    j=i+1

            #print("stack",stack)
            return "".join(sorted(stack)[::-1])
        return dfs(S)
sol = Solution()
test_data = [ "11011000","10" ]
for d in test_data:
    print(sol.makeLargestSpecial(d))

l = ['10', '1100']
print(sorted(l)[::-1])