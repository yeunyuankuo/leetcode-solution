import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # time: O(81)
        # space: O(27), 9 rows, 9 cols, 9 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[r//3 * 3 + c//3]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[r//3 * 3 + c//3].add(board[r][c])
        return True