class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        '''
         set1 for row hash
            row_n 0_0 , 0_1, 1_0, ..... ,should not repeat.
         set2 for col hash
            as the same as row
         set3 for 33box
            boxId_n 9x9 -> there are 3, 3x3 boxes
            0_1,0_2....
        '''
        map1 = {}
        map2 = {}
        map3 = {}

        for y in range(0,9):
            for x in range(0, 9):
                print(x,y)
                if board[y][x] == '.':
                    continue
                if (map1.get(str(y) + board[y][x]) == None and
                    map2.get(str(x) + board[y][x]) == None and
                    map3.get(str(x/3)+str(y/3) + board[y][x]) == None):
                    map1[str(y) + board[y][x]] = 1
                    map2[str(x) + board[y][x]] = 1
                    map3[str(x/3)+str(y/3) + board[y][x]] = 1
                else:
                    return False
        return True
sol = Solution()

test1 = [
  ["5","3","2",".","7","6","1","9","8"],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

test2 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
test3 = [
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."]
]

test4 = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]

test5 = [
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".","9",".",".",".",".",".",".","1"],
    ["8",".",".",".",".",".",".",".","."],
    [".","9","9","3","5","7",".",".","."],
    [".",".",".",".",".",".",".","4","."],
    [".",".",".","8",".",".",".",".","."],
    [".","1",".",".",".",".","4",".","9"],
    [".",".",".","5",".","4",".",".","."]]
#print("test 1",sol.isValidSudoku(test1) )
#print("test 2",sol.isValidSudoku(test2) )
#print("test 3",sol.isValidSudoku(test3) )
#print("test 4",sol.isValidSudoku(test4) )
print("test 5",sol.isValidSudoku(test5) )

a= [11,22,33]
for i, x in enumerate(a):
    print(i,x)