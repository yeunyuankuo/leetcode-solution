def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    # time: O(N)
    # space: O(1)
    maxCount, count = 0, 0
    for num in nums:
        if num == 1:
            count += 1
            maxCount = max(maxCount, count)
        else:
            count = 0
    return maxCount