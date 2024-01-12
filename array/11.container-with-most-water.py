def maxArea(self, height: list[int]) -> int:
    # time: O(N)
    # space: O(N)
    l, r = 0, len(height)-1
    maxSum = 0
    while l < r:
        currSum = (r-l) * min(height[l], height[r])
        maxSum = max(maxSum, currSum)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return maxSum