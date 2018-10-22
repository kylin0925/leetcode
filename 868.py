class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        new_matrix = [ [0 for i in range(m)] for i in range(n)  ]

        #print new_matrix
        for i in range(m):
            for j in range(n):
                
                new_matrix[j][i] = A[i][j]
                #print i,j,A[i][j],new_matrix[j][i]
        #print new_matrix
        return new_matrix
sol = Solution()
test_data = [ [[1],[2]], [[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6]] ]
for d in test_data:
    print sol.transpose(d)
