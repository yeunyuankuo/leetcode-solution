class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1 for _ in range(size)]
        print(dp)

        for i in range(size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)