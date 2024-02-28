class Solution:
    # Time Complexity: O(m * n * 4^k), m: the number of rows in the board.
    # n: the number of columns in the board. k: the length of the word.
    # The main function exist iterates over all cells of the board, which takes O(m * n) time.
    # Inside the dfs function, each cell is visited at most once, and each recursive call
    # explores up to four neighboring cells. The maximum number of recursive calls for
    # each cell is bounded by the length of the word k. Hence, the time complexity of
    # the DFS part of the algorithm is O(4^k). Overall, the time complexity is
    # dominated by the DFS traversal, so it is O(m * n * 4^k).
    #
    # Space Complexity: O(k)
    def exist(self, board: list[list[str]], word: str) -> bool:
        w = len(board)
        h = len(board[0])

        def dfs(i, r, c, visited):
            if i == len(word):
                return True

            if r < 0 or r >= w or c < 0 or c >= h or board[r][c] != word[i]:
                return False

            if (r,c) not in visited and board[r][c] == word[i]:
                visited.add((r,c))
                res = (dfs(i + 1, r + 1, c, visited) or
                    dfs(i + 1, r - 1, c, visited) or
                    dfs(i + 1, r, c + 1, visited) or
                    dfs(i + 1, r, c - 1, visited))
                visited.remove((r,c))
                return res

            return False
                
        for r in range(w):
            for c in range(h):
                if board[r][c] == word[0] and dfs(0, r, c, set()):
                    return True

        return False