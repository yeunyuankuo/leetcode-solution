def containsDuplicate(self, nums: list[int]) -> bool:
    # time = O(N)
    # space = O(N)
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False