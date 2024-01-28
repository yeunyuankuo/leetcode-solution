def trap(self, height: list[int]) -> int:
    # time: O(N)
    # space: O(1)
    res = 0
    l, r = 0, len(height)-1
    maxL, maxR = height[0], height[-1]

    while l < r:
        if height[l] < height[r]:
            currWater = maxL - height[l]
            res += max(0, currWater)
            maxL = max(maxL, height[l])
            l += 1
        else:
            currWater = maxR - height[r]
            res += max(0, currWater)
            maxR = max(maxR, height[r])
            r -= 1

    return res