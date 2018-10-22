class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # print(matrix)
        h = len(matrix)
        w = len(matrix[0])
        #print(h,w)
        for i in range(0,w):
            n0 = matrix[0][i]
            for j in range(1, h):
                #print("%d %d" % (j,i+j))
                if j+i < w and matrix[j][j+i] != n0:
                    return False

        for i in range(1,h):
            n0 = matrix[i][0]
            #print(i,0)
            for j in range(1,h):
                if j+i < h and j < w:
                    #print("-> %d %d" %(j+i,j))
                    if matrix[j + i ][j] != n0:
                        return False
        return True


sol = Solution()
test_data = [[[41,45],[81,41],[73,81],[47,73],[76,47],[79,76]],
             [[83], [64], [57]],
             [[11, 74, 0, 93],
              [40, 11, 74, 7]],
             [[18], [66]],
             [[1, 2],
              [2, 2]
              ],
             [
                 [1, 2, 3, 4],
                 [5, 1, 2, 3],
                 [9, 5, 1, 2]
             ]
             ]
for d in test_data:
    print(sol.isToeplitzMatrix(d))
