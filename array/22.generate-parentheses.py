def generateParenthesis(self, n: int) -> list[str]:
    # time: O(2 ^2N), time complexity in this case is O(k^n),
    # where 'k' is the number of choices at each position, 
    # and 'n' is the total number of positions. In this case, k = 2.
    # b/c there are 2 choices '(' and ')'. n = 2N, where N is the number
    # of positions, and 2 is b/c each position final string can either be
    # '(' or ')'.
    #
    # space: O(N)
    stack = []
    res = []

    def backtracking(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
        
        if openN < n:
            stack.append('(')
            backtracking(openN + 1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(')')
            backtracking(openN, closeN + 1)
            stack.pop()

    backtracking(0,0)
    return res