class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for c in J:
            res += S.count(c)
        return res
sol = Solution()
test_data = [ ["aA", "aAAbbbb"] , ["zZ", "ZZ"]]
for d in test_data:
    print(sol.numJewelsInStones(d[0],d[1]))
