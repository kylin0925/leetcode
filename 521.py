class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a),len(b))
sol = Solution()
test_data = [["aba", "aba"] ]
for d in test_data:
    print sol.findLUSlength(d[0],d[1])
