class Solution:
    def integerBreak(self, n: int) -> int:
        ans =1
        for i in range(2,n):
            q = n//i # 12/5 = 2 r = 2
            r = n % i  # 5-2=3 2**3=8 222 33
                        # 12 - (2*3) = 6/2 =3
            p2 = 0
            p3 =0
            if r > 0:
                p2 = n - q*(i-r)
                p3 = p2/r

            ans = max(ans, int(q**(i-r)*(p3**r)))
            #print(ans)

        return ans
print(Solution().integerBreak(2))
print(Solution().integerBreak(3))
print(Solution().integerBreak(4))
print(Solution().integerBreak(5))
print(Solution().integerBreak(6))
print(Solution().integerBreak(7))
print(Solution().integerBreak(8))
print(Solution().integerBreak(9))
print(Solution().integerBreak(10))
print(Solution().integerBreak(11))
print(Solution().integerBreak(12))
print(Solution().integerBreak(20))
print(Solution().integerBreak(59))
