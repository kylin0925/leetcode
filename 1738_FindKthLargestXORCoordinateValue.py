from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        prexor = [0 for i in range(m*n)]

        tmp = 0
        for i in range(n):
            prexor[i] = tmp ^ matrix[0][i]
            tmp = prexor[i]
        #print(prexor)
        tmp = 0
        for i in range(m):
            prexor[i*n] = tmp ^ matrix[i][0]
            tmp = prexor[i*n]
        #print(prexor)

        for i in range(1,m):
            for j in range(1,n):
                tmp = prexor[ (i-1)*n + j-1] ^prexor[ (i-1)*n + j] ^ prexor[i*n + j-1] ^ matrix[i][j]
                prexor[i*n+j] = tmp
        prexor.sort(reverse=True)
        #print(prexor)
        return prexor[k-1]


print(1738)

print(Solution().kthLargestValue( matrix = [[5,2],[1,6]], k = 1))
print(Solution().kthLargestValue( matrix = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
