class Solution:
    # Brute force solution - TLE
    # time: O(2^n)
    # space: O(n)
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        size = len(nums)

        def dfs(i, currSum):
            if i == size:
                if currSum == target:
                    return 1
                else:
                     return 0
            return dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])

        return dfs(0, 0)
    
    # Memoization Solution with DP
    # time: O(2^n)
    # space: O(n)
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        size = len(nums)
        table = dict()

        def dfs(i, currSum):
            if i == size:
                if currSum == target:
                    return 1
                else:
                     return 0

            if (i, currSum) in table:
                return table[(i, currSum)]
            
            count = dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])
            table[(i, currSum)] = count
            return count

        return dfs(0, 0)
