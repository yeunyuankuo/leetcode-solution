import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # time: O(81), 9x9 grid
        # space: O(27), 9 rows, 9 cols, 9 boxes
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in row[r] or
                    board[r][c] in col[c] or
                    board[r][c] in box[(r//3, c//3)]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                box[(r//3, c//3)].add(board[r][c])
        return True