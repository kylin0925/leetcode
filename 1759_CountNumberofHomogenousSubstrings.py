class Solution:
    def countHomogenous(self, s: str) -> int:
        strlen = len(s)
        i=0
        ans = 0
        while i <strlen:
            c = s[i]
            cnt = 0
            while i < strlen and s[i]==c:
                cnt+=1
                i+=1
            ans +=(cnt+1)*cnt >> 1
        return ans % (10**9+7)
print(Solution().countHomogenous(s = "abbcccaa"))
print(Solution().countHomogenous(s = "xy"))
print(Solution().countHomogenous(s = "zzzzz"))
print(Solution().countHomogenous(s = "aabaa"))
print(Solution().countHomogenous(s = "a"*100000))