def threeSum(self, nums: list[int]) -> list[list[int]]:
    # time: O(NlogN) + O(N^2), O(NlogN): b/c we sorted the list, O(N^2): b/c there's a nested for loop
    # spcae: O(M), M is number of triplets
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        # skip positive value, b/c everything from this point would add up to be > 0
        if a > 0:
            break
        
        # skip duplicate first value
        if i > 0 and nums[i-1] == a:
            continue
        
        l, r = i+1, len(nums)-1
        while l < r:
            threesum = a + nums[l] + nums[r]
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res