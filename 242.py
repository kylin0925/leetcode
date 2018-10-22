class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """ 
        ss = [c for c in s]
        ss.sort()
        tt = [c for c in t]
        tt.sort()
        return ss == tt
sol = Solution()
test_data = [ ["anagram",  "nagaram"], ["rat","cat"] ]
for d in test_data:
    print sol.isAnagram(d[0],d[1])
