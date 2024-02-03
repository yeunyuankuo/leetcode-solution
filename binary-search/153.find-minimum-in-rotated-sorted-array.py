class Solution:
    def findMin(self, nums: list[int]) -> int:
        # time: O(logN)
        # space: O(1)
        l, r = 0, len(nums) - 1
        minVal = float("inf")

        while l <= r:
            mid = (l + r) // 2
            minVal = min(minVal, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return minVal