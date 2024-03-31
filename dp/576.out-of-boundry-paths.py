class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # time: O(4^maxMove)
        # space: O(m*n*maxMove)
        mod = 10 ** 9 + 7
        table = dict()
        directions = {(1,0), (-1,0), (0,-1), (0,1)}

        def dfs(r, c, currMove):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1

            if currMove == maxMove:
                return 0

            if (r, c, currMove) in table:
                return table[(r, c, currMove)]

            res = 0
            for d in directions:
                res += dfs(r + d[0], c + d[1], currMove + 1)
                res %= mod

            table[(r, c, currMove)] = res
            return res

        return dfs(startRow, startColumn, 0)