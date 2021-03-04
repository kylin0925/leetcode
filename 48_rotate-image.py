from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # swap dia
        n = len(matrix[0])
        for i in range(n):
            for j in range(n-i-1):
                swidx = n-j-1 -i
                print(swidx)
                matrix[i][j],matrix[i + swidx][j+ swidx] = matrix[i + swidx][j+ swidx],matrix[i][j]
            print(i,matrix)
        print(matrix)
        #swap upside down mirror
        for i in range(n//2):
            offy = n - i - 1
            for j in range(n):
                matrix[i][j], matrix[offy][j] = matrix[offy][j], matrix[i][j]

        print(matrix)

test_data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

sol = Solution()
ans = sol.rotate(test_data)
print(test_data)