class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]

        for row, col in start:
            s = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    item = board[i][j]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True
        
        