class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """  
        table = {}
        i = 0
        s_len = len(s)
        while i < s_len:
            if table.has_key(s[i]) == False:
                if t[i] not in table.values():
                    table[s[i]] = t[i]
                else:
                    return False
            else:
                if table[s[i]]!=t[i]:
                    return False
            i+=1    
        return True        
sol = Solution()
test_data = [ ["abab","baba"], ["a","a"], [ "baa", "cfa"],[ "aba", "baa"], [ "ab", "aa"],["foo", "bar"],["paper", "title"]]
# t t f f f f t 
for d in test_data:
    print sol.isIsomorphic(d[0],d[1])
