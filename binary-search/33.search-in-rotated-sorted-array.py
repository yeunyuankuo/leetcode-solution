def search(self, nums: list[int], target: int) -> int:
    # time: O(logN)
    # space: O(1)
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        # case 1: subarray on mid's left is sorted
        if nums[l] <= nums[mid]:
            if target > nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        # case 2: subarray on mid's right is sorted
        else:
            if target < nums[r] and target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

    return -1