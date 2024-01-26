class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # time: O(S)
        # space: O(T)
        
        # create char count dict for t
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1

        # create a curr char count dict for keeping track of curr char
        curr = {}

        l = 0
        minL = float("inf")
        res = ""
        needmatch = len(count) # needmatch is the number of char count we need to match
        for r in range(len(s)):
            c = s[r]
            if c in count:
                curr[c] = curr.get(c, 0) + 1
                if curr[c] == count[c]:
                    needmatch -= 1

            # if we have all the char counts that need matching,
            # we can move the left border to adjust the window
            while needmatch == 0:
                if minL > r - l + 1:
                    res = s[l:r + 1]
                    minL = r - l + 1
                if s[l] in count:
                    curr[s[l]] -= 1
                    if curr[s[l]] < count[s[l]]:
                        needmatch += 1
                l += 1
                
        return res