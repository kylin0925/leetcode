class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = [c for c in ransomNote]
        m = [c for c in magazine]
        r.sort()
        m.sort()
        
        res = True

        #print r,m
        if len(r) > len(m):
            return False

        mag_table = [0 for i in xrange(26)]
        for c in m:
            mag_table[ord(c) - ord('a')] +=1
        
        i =0      
        while i < len(r) :
            #print i,mag_table
            if mag_table[ord(r[i]) - ord('a')] > 0:
                mag_table[ord(r[i]) - ord('a')]-=1
            else:
                return False
            i+=1
        return True
sol = Solution()
test_data = [["aa","ab"],["bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"],["aa", "ab"], ["aa", "aab"],["abc","cba"],["a",""],["",""],["abcde","a"],["aaaa","aa"] ]
for d in test_data:
    print sol.canConstruct(d[0],d[1])
