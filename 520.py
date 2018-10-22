class Solution(object):
    def AllCap(self,word):
        return word == word.upper()
    def AllLower(self,word):
        return word == word.lower()
    def FirstCap(self,word):
        f = word[0].upper()
        remaid_word = word[1:].lower()
        return word == f+remaid_word
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        return self.AllCap(word) or self.AllLower(word) or self.FirstCap(word)
sol = Solution()
test_data = [ "USA","aBCDE","Accc","abc","","GooG"]
for d in test_data:
    print sol.detectCapitalUse(d)
