class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        #print(widths,S,len(S),26 * 10%100)
        totalWidth = 0
        lines = 1

        for c in S:
            totalWidth += widths[ord(c) - ord('a') ]
            if totalWidth > 100:
                lines +=1
                totalWidth = widths[ord(c) - ord('a') ]

        return  [lines,totalWidth]
sol = Solution()
test_data = [  [[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz"],
               [[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"],
               [[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "a"]
               ]
for d in test_data:
    print(sol.numberOfLines(d[0],d[1]))
