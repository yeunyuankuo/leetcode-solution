class Solution:
    # time: O(N!), b/c the N * N-1 * N-2 * N-3 ... is the number of combinations for N queens
    # space: O(N^2)
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [ ["."] * n for _ in range(n)]
        res = []

        cols = set()
        posDiag = set()
        negDiag = set()

        def bt(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                bt(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        bt(0)
        return res