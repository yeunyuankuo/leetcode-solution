def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    # time: O(logN*M)
    # space: O(1)

    # find the row that could contain target
    row = len(matrix)-1
    for r in range(len(matrix)):
        if matrix[r][0] == target:
            return True
        elif matrix[r][0] > target and r > 0:
            row = r - 1
            break

    # loop through row to find target
    l, r = 0, len(matrix[row])-1
    while l <= r:
        mid = l + ((r-l)//2)
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False