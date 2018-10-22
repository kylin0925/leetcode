class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        table_s = [ 0 for i in xrange(256)]
        table_t = [ 0 for i in xrange(256)]
        for c in s:
            table_s[ord(c)]+=1
        for c in t:
            table_t[ord(c)]+=1
            
        for i in xrange(256):
            if table_s[i] != table_t[i]:
                return chr(i)
sol = Solution()
test_data = [["abcd","abcde" ],["a","aa" ],["aabb","aeabb" ]]
for d in test_data:
    print sol.findTheDifference(d[0],d[1])
