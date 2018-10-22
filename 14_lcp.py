class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 1
        max_len = 0
        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        for s in strs:
            if len(s) > max_len:
                max_len = len(s)
        
        res = ""
        print max_len
        while i <= max_len:
            tmp = s[0:i]
            cnt = 0
        
            for s in strs:
                if tmp == s[0:i]:
                    cnt+=1
            
            #print cnt
            if cnt==n:
                res = s[0:i]
               
            i=i+1

        return res
s = Solution()
print s.  longestCommonPrefix(["b","c"])      