from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direct = [[0, 1],
                  [1, 0],
                  [0, -1],
                  [1, 0]]
        res = []

        x=y=0
        m = len(matrix)
        n = len(matrix[0])
        total = 0

        while total < m*n:
            while x<n:
                if matrix[y][x] == -1:
                    break
                res.append(matrix[y][x])
                matrix[y][x] =-1
                total+=1
                x+=1
            x-=1
            y+=1
            while y<m:
                if matrix[y][x] == -1:
                    break
                res.append(matrix[y][x])
                matrix[y][x] = -1
                total += 1
                y+=1
            x-=1
            y-=1
            while x>-1:
                if matrix[y][x] == -1:
                    break
                res.append(matrix[y][x])
                matrix[y][x] = -1
                total += 1
                x-=1
            x+=1
            y-=1
            while y>-1:
                if matrix[y][x] == -1:
                    break
                res.append(matrix[y][x])
                matrix[y][x] = -1
                total += 1
                y-=1

            y+=1
            x+=1
        #print(res)
        return res
data = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
data2=[
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9 ,10],
  [11,12,13,14,15],
  [16,17,18,19,20],
[16,17,18,19,20]
]
sol = Solution()
ans = sol.spiralOrder(data2)


