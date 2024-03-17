class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(start, subset):
            res.append(subset[:])
            
            for i in range(start, len(nums)):
                # When i == start, it means we are considering the first occurrence of an
                # element at the current level of recursion. In this case, even if it's a duplicate,
                # we want to include it in the subset to ensure that we explore all possibilities.
                #
                # When i > start, it means we are considering duplicate elements that come after the
                # first occurrence (start). If we encounter a duplicate in this scenario, we want to
                # skip it to avoid generating duplicate subsets.
                #
                # By adding the condition i > start, we ensure that we only skip duplicates that occur
                # after the initial occurrence of an element in the current level of recursion, allowing
                # us to generate unique subsets.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                subset.append(nums[i])
                bt(i + 1, subset)
                subset.pop()

        bt(0, [])
        return res