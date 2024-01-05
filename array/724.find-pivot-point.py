def pivotIndex(self, nums: list[int]) -> int:
    # time: O(N)
    # space: O(1)
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    curr_sum = 0
    for i in range(len(nums)):
        if curr_sum * 2 + nums[i] == sum:
            return i
        curr_sum += nums[i]
    return -1