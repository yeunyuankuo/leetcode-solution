class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # time: O()
        # space: O(N)
        res = []

        def bt(start, subset):
            res.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                bt(i + 1, subset)
                subset.pop()

        bt(0, [])
        return res