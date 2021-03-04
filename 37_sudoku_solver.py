from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.isFinsh = False
        def check(n,x,y,board):

            for e in board[y]:
                if e == n:
                    return False
            for i in range(9):

                if board[i][x] == n:
                    return False
            sx = int(x/3) * 3
            sy = int(y/3) * 3
            for i in range(sy,sy+3):
                for j in range(sx,sx+3):
                    if board[i][j] == n:
                        return False
            return True
        def checkFinish(board):

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                       return
            self.isFinsh = True
        def solve(board):
            #print(board)
            checkFinish(board)
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.' and not self.isFinsh:
                        for x in range(1,10):
                            if check(str(x),j,i,board):
                                board[i][j] = str(x)
                                solve(board)
                                if not self.isFinsh:
                                    board[i][j] = '.'

                        return

        solve(board)
        #print(board)
sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol.solveSudoku(board)
print(board)