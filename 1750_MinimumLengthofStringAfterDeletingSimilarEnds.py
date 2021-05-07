class Solution:
    def minimumLength(self, s: str) -> int:

        l = 0
        r = len(s)-1
        while l < r and s[l] == s[r]:
            c = s[l]
            #print(l, r,c)
            while s[l] == c and l < r:
                l+=1
            while s[r] == c and l <= r:
                r-=1

        #print("*",l, r)
        return r-l+1

print(Solution().minimumLength(s="bab"))
print(Solution().minimumLength(s="cabaabac"))
print(Solution().minimumLength(s="bbbbbc"))
print(Solution().minimumLength(s="aabccabba"))
print(Solution().minimumLength(s="a"))

# 01234567
# cabaabac