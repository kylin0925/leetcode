class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def getMorseTransform(word):
            morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            res =""
            for c in word:
                res += morsecode[ord(c)-ord('a')]
            return res
        wordsTomorse=[]
        for word in words:
            #print(word)
            wordsTomorse.append(getMorseTransform(word))

        filterlist = []

        for wtm in wordsTomorse:
            if filterlist.count(wtm) == 0:
                filterlist.append(wtm)

        return len(filterlist)
sol = Solution()
test_data = [["gin","zen", "gig", "msg"],['eeee','h']]
for d in test_data:
    print(sol.uniqueMorseRepresentations(d))