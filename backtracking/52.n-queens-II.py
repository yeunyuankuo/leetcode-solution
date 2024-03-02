class Solution:
    def totalNQueens(self, n: int) -> int:
        # time: O(N * N!), b/c N is the number of cells a queen can choice in a row and
        # the N-1 * N-2 * N-3 ... is the number of configurations to check for the cells in different row
        # space: O(N), for maintaining cols and posDiag and negDiag sets
        res = 0

        cols = set()
        posDiag = set()
        negDiag = set()

        def bt(r):
            nonlocal res

            if r == n:
                res += 1
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                bt(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        bt(0)
        return res