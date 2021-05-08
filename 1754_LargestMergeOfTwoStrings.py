class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1len = len(word1)
        w2len = len(word2)

        res = ""
        while len(word1) > 0 and len(word2) > 0:
            if word1>word2:
                res+=word1[0]
                word1=word1[1:]
            else:
                res += word2[0]
                word2 = word2[1:]
        if len(word1)>0:
            res+=word1
        if len(word2) > 0:
            res+=word2
        return res
print(Solution().largestMerge( word1 = "cabaa", word2 = "bcaaa") == "cbcabaaaaa")
print(Solution().largestMerge( word1 = "abcabc", word2 = "abdcaba") == "abdcabcabcaba")
print(Solution().largestMerge( word1 = "a", word2 = "b") == "ba")
print(Solution().largestMerge( word1 = "a"*3000, word2 = "b"*3000) )