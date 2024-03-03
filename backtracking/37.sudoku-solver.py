class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        # time: O((9!)^9), every row you have 9 choice on the first cell, 8 choice on the second cell, etc.
        # this means each row you will have 9x8x7...x1 or 9! choices. And since we have 9 rows this makes
        # the time complexity (9!)^9
        #
        # space: O(9*9)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        solved = False

        # initialize the board with values already given (none empty cells)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c])
                    rows[r].add(num)
                    cols[c].add(num)
                    box_id =  (r // 3 * 3) + c // 3
                    boxes[box_id].add(num)

        def bt(r, c):
            nonlocal solved
            if r == 9:
                solved = True
                return

            # calculate next empty location (row, col)
            next_r = r + (c + 1) // 9 # this makes sure r only +1 when c reaches index 8
            next_c = (c + 1) % 9 # this makes sure c is kept within 0~8
             
            # if not empty cell, try next empty cell
            if board[r][c] != '.':
                bt(next_r, next_c)
            else:
                for num in range(1, 10):
                    box_id = (r // 3 * 3) + c // 3
                    if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                        # add num to visited and update the board
                        rows[r].add(num)
                        cols[c].add(num)
                        boxes[box_id].add(num)
                        board[r][c] = str(num)

                        # do backtracking on next empty cell
                        bt(next_r, next_c)
                        
                        # if backtracking didn't solve it, clean up previous(go back to one step before)
                        if not solved:
                            rows[r].remove(num)
                            cols[c].remove(num)
                            boxes[box_id].remove(num)
                            board[r][c] = '.'

        bt(0, 0)