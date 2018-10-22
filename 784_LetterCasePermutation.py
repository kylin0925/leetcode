class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        letter_cnt = 0
        for c in S:
            if c.isalpha():
                letter_cnt+=1
        #print(letter_cnt)
        n = 2 ** letter_cnt

        res = []
        for i in range(n):
            to_upper = format(i,"0"+str(letter_cnt)+"b")
            j = letter_cnt -1
            #print(j,to_upper)
            tmpS = S
            while j >= 0:
                if to_upper[j] == "1":
                    #print("to upper",j)
                    k = 0
                    cnt = 0
                    while k < len(S):
                        if S[k].isalpha():
                            cnt+=1
                        if cnt == j+1 and S[k].isalpha():
                            if S[k].islower():
                                tmpS = tmpS[0:k] + tmpS[k].upper() + tmpS[k+1:]
                            else:
                                tmpS = tmpS[0:k] + tmpS[k].lower() + tmpS[k+1:]
                        k+=1

                j -= 1
            res.append(tmpS)
        #print("res", tmpS)
        return  res

sol = Solution()
test_data = ["a1b2","12345","a","A","2z4","abcdefghijkl","1ab","ab1","1",""]

for d in test_data:
    print(sol.letterCasePermutation(d))