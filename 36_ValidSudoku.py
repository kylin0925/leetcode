class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #valid echo row
        def valid(row):
            flag = {}
            for n in row:
                if n ==".":
                    continue
                if flag.get(n) == None:
                    flag[n] = 1
                else:
                    return False
            return True
        def validBox(x,y):
            flag = {}
            for j in range(y,y+3):
                for i in range(x, x + 3):
                    #print(j,i)
                    n = board[j][i]
                    if n == ".":
                        continue
                    if flag.get(n) == None:
                        flag[n] = 1
                    else:
                        return False
            return True
        isValid = True
        for i in range(9):
            row = board[i]
            isValid &= valid(row)
            print(isValid)
            col = [board[x][i] for x in range(9)]
            isValid &= valid(col)
            print(isValid)
        if isValid == False:
            return  False

        for y in range(0,7,3):
            for x in range(0, 7, 3):
                #print("check start ",x,y)
                isValid &= validBox(x,y)
                print(x,y,isValid)
        if isValid == False:
            return  False
        #valid echo col
        #valid echo 3x3 box

        return True
sol = Solution()

test1 = [
  ["5","3","2","4","7","6","1","9","8"],
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
  ["8","3",".",".","7",".",".",".","."],
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
#print("test 1",sol.isValidSudoku(test1) )
#print("test 2",sol.isValidSudoku(test2) )
#print("test 3",sol.isValidSudoku(test3) )
print("test 4",sol.isValidSudoku(test4) )