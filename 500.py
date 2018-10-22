class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard_row = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        res = []
        for word in words:
            w = word.lower()
            if len(w) ==0:
                continue
            i = 0
            for i in xrange(3):
                if w[0] in keyboard_row[i]:
                    break
            j =0
            #print "in row",i,w
            while j < len(w):
                if w[j] not in keyboard_row[i]:
                    break
                j+=1    
            #print j        
            if j ==len(w):
                res.append(word)
        return res        
sol = Solution()
test_data = [["Hello", "Alaska", "Dad", "Peace",""] ]
for d in test_data:
    print sol.findWords(d)
