def longestConsecutive(self, nums: list[int]) -> int:
    # time: O(N)
    # spcae: O(N)
    exist = set(nums)    
    longest = 0
    for n in nums:
        if (n-1) not in exist:
            length = 1
            while (n + length) in exist:
                length += 1
            longest = max(longest, length)
    return longest