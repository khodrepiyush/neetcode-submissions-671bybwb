class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            set1=set()
            set2=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in set1:
                        return False
                    set1.add(board[i][j])
                if board[j][i]!='.':
                    if board[j][i] in set2:
                        return False
                    set2.add(board[j][i])
        row=0
        col=0
        for i in range(9):
            set1=set()
            for j in range(3):
                for k in range(3):
                    row=(i//3)*3+j
                    col=(i%3)*3+k
                    if board[row][col]!='.':
                        if board[row][col] in set1:
                            return False
                        else:
                           set1.add(board[row][col]) 
        return True
                



        