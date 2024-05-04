class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # time: O(n * m), n = len(nums), m = target
        # space: O(m), m = target
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        # for every w, we want to calculate the combination to sum to w.
        # which means dp[w] = dp[w-n1] + dp[w-n2] + dp[w-n3] ... + dp[w-nums[-1]], as long as w >= n.
        # Let say that nums: [1, 2, 3], and target is 4.
        # then dp[4] = d[4-1] + dp[4-2] + dp[4-3]

        for w in range(target + 1): # starting from 0 to do a bottom-up DP
            for n in nums:
                if w >= n:
                    dp[w] += dp[w - n]

        return dp[target]