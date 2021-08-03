class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        tbl = [1,10]
        if n <=1:
            return tbl[n]

        nine = 9
        for j in range(2,n+1):
            ans = 9
            for i in range(j-1):
                ans *= (nine-i)
                #print(ans,nine-i)
            ans = ans + tbl[-1]
            tbl.append(ans)
        #print(tbl)
        return tbl[-1]

print(Solution().countNumbersWithUniqueDigits(4))
