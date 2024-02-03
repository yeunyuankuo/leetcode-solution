import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # time: O(N + log(K)), where K is maximum pile size
        # space: O(1)

        # find biggest pile or k
        maxPile = piles[0]
        for p in piles:
            maxPile = max(maxPile, p)

        # binary search the minimum k
        l, r = 1, maxPile
        minK = float("inf")
        while l <= r:
            k = (l + r) // 2
            hourUsed = 0
            for p in piles:
                hourUsed += math.ceil(p / k)
            if hourUsed <= h:
                minK = min(minK, k)
                r = k - 1
            else:
                l = k + 1
            
        return minK