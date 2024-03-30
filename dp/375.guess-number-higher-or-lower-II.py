class Solution:
    def getMoneyAmount(self, n: int) -> int:
        def print_matrix(matrix):
            for row in matrix:
                print(" ".join(map(str, row)))
            print()
        # time: O(n^3)
        # space: O(n^2)
        # matrix[i][j]: stores the minimum amount needed for a subrange(i,j) of numbers
        # i -> starting point of the subrange of numbers being considered
        # j -> ending point of the subrange of numbers being considered
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        print_matrix(dp)

        # length is the length of the subrange.
        # length is used to determine the end point of the subrange within the inner loop.
        # length start from 2 because subrange with length of 1 doesn't need guessing.
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
                print_matrix(dp)

                # - iterate through all possible guesses(k) in range(i,j-1).
                # range(i,j-1) and not range(i,j) because By iterating k from i to j - 1, 
                # the algorithm systematically explores guesses starting from the smaller 
                # numbers within the given subrange [i, j]. This approach aligns with the 
                # strategy of minimizing the amount spent on guesses, as it's more efficient
                # to start guessing with smaller numbers and progressively increase.
                # And when we guessed i ~ j-1 we would know whether j is the correct answer or not,
                # so we don't need to guess j.
                #
                # - we want the max out of the amount to win in "the left of k", subrange(i, k-1),
                # or the amount to win in "the right of k", subrange(k+1, j).
                #
                # - the min of current subrange(i,j) and the max we got above +k will be the new amount for subrange(i,j)
                # +k because if we guess k then we need to add the value k
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], max(dp[i][k - 1] + k, dp[k + 1][j] + k))
                    print_matrix(dp)

        # get the min amount needed to win in subrange(1, n)
        return dp[1][n]
    
    