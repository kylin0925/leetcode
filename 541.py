class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s == "":
            return ""
        if k ==0:
            return s
        s_len = len(s)
        i = 0
        res = ""
        while i < s_len:
            
            tmp = ""
            if i ==0 or i % (2*k) ==0:
                tmp = s[i:i+k][::-1] 
            else:
                tmp = s[i:i+k]
            
            res +=tmp
            i+=k
            #print i,res
        return res
sol = Solution()
test_data = [[ "abcdefg", 2],[ "abcdefg", 0],[ "abcdefg", 4]]
for d in test_data:
    print sol.reverseStr(d[0],d[1])
