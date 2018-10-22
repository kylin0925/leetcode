class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        table = [ 0 for i in xrange(256)]
        for c in s:
            table[ord(c)]+=1
        idx = 0
        for c in s:
            if table[ord(c)] == 1:
                return  idx
            idx+=1
        return -1
        
sol = Solution()
test_data = ["leetcode", "loveleetcode","aa" ]
for d in test_data:
    print sol.firstUniqChar(d)
