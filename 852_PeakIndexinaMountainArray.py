class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """ 
        data_len = len(A)
        i = 0
        while i < data_len:
            if A[i]> A[i+1]:
                break
            i+=1
        return i
sol = Solution()
test_data = [ [0,2,1,0], [0,1,0],[0,0,0,1,2,3,1,0,0] ]
for d in test_data:
    print sol.peakIndexInMountainArray(d)
