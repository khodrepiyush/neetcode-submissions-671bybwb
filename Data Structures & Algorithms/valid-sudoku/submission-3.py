class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {x: set() for x in range(9)}
        cols = {x: set() for x in range(9)}
        boxes = {x: set() for x in range(9)}

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])

                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])

                box = 3*(i//3) + j//3
                print(box)
                if board[i][j] in boxes[box]:
                    return False
                boxes[box].add(board[i][j])
        return True

            


        
        
        