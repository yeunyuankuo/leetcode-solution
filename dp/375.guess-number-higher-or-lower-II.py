class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # time: O(n^3)
        # space: O(n^2)
        # matrix[i][j]: stores the minimum amount needed for a subrange(i,j) of numbers
        # i -> starting point of the subrange of numbers being considered
        # j -> ending point of the subrange of numbers being considered
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        # length is the length of the subrange.
        # length is used to determine the end point of the subrange within the inner loop.
        for length in range(2, n + 1):
            # i -> starting point
            for i in range(1, n + 1):
                # j -> ending point
                j = i + length - 1

                # if ending point exceeds n we exit
                if j > n:
                    break
                
                # first give max val to subrange(i,j)
                dp[i][j] = float('inf')

                # then iterate through all possible guesses(k) in range(i,j)
                # we want the max out of the amount to win in subrange(i, k-1) or the amount to win in subrange(k+1, j)
                # the min of current subrange(i,j) and the max we got above will be the new amount for subrange(i,j)
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], max(dp[i][k - 1] + k, dp[k + 1][j] + k))

        # get the min amount needed to win in subrange(1, n)
        return dp[1][n]