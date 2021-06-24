class Solution:
    def beautySum(self, s: str) -> int:
        def max_min_diff(arr):
            max_n = -1
            min_n = 10**9+7
            for n in arr:
                if n > max_n:
                    max_n =n
                if n!=0 and min_n > n:
                    min_n = n
            return max_n - min_n

        str_len = len(s)
        tbl = [[0 for i in range(26)] for i in range(str_len)]
        for i in range(len(s)):
            c = ord(s[i]) -ord('a')
            for j in range(i, str_len):
                tbl[j][c] +=1
        #for r in tbl:
        #    print(r)
        
        bsum = 0
        for l in range(str_len,2,-1):
            bsum += max_min_diff(tbl[l-1])
            for i in range(1,str_len):
                if i+l-1 < str_len:
                    tmp = [x for x in tbl[i+l-1]]
                    for j in range(26):
                        tmp[j]-=tbl[i-1][j]
                    diff =  max_min_diff(tmp)
                    #print(l,"diff",diff)
                    bsum += max_min_diff(tmp)
                else:
                    break
            #print(l,bsum)

        return bsum
print(Solution().beautySum("aabcb"))
print(Solution().beautySum("aabcbaa"))
print(Solution().beautySum("a"))
print(Solution().beautySum("ab"))
print(Solution().beautySum("bbc"))
