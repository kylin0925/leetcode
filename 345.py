class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """  
        vowels = "aeiouAEIOU"
        tmp =""
        s_len = len(s)
        for i in xrange(s_len):
            c = s[i]
            if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U" :
                tmp+=c
                
        tmp = tmp[::-1]
        i = 0
        res = ["" for j in xrange(s_len)]
               
        for j in xrange(s_len):
            c = s[j]          
            if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U" :
                res[j]=tmp[i]
                i+=1
            else:
                res[j]=s[j]
        return "".join(res)
sol = Solution()
test_data = [ "hello", "leetcode","world","hjklm","aA",]
for d in test_data:
    print sol.reverseVowels(d)
