class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """  
        num = int( "".join([str(x) for x in digits]))
        res = str(num+1)        
        reslist = [int(res[x]) for x in range(len(res))]         
        return reslist
sol = Solution()
test_data = [[1,2,3],[4,3,2,1],[9,9] ]
for d in test_data:
    print sol.plusOne(d)
