import collections

def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    output = []
    q = collections.deque()  # index
    l = r = 0

    # time: O(n)
    # spcae: O(n)
    while r < len(nums):
        # pop smaller values from q
        while q and nums[q[-1]] < nums[r]:
            p = q.pop()
        q.append(r)

        # remove left val from queue, b/c the window have already moved
        # this can happen when queue's corresponding val (e.g. nums[q[i]]) are in decreasing order
        # so no element got popped from the queue, and the number exceeded the size k. Then we 
        # need to keep track of the size of the queue by monitoring whether q[0] is still within window.
        if l > q[0]:
            q.popleft()

        # append max num to output only when (r + 1) >= k
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output