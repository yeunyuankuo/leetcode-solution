class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use slow/fast pointer to find the first intersection (where two pointer points to same index)
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # start from 0 index again and iterate the same distance as slow to find the duplicate result
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
        return nums[slow]