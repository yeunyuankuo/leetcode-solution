class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # time: O(N * 2^N), N is the length of string s. In worst case, there could be 2^N possible number of nodes
        # in the search tree, which is the number of possible partitionings. N * 2^N because for each partitioning
        # substring we need to check if its a palindrome, so times O(N) for palindrome checking.
        #
        # space: O(N), N is the length of string s.
        res = []
        temp = []

        def dfs(i):            
            # if i >= len(s) we know that we have exhasuted all options
            # and we may return the temp to res
            if i >= len(s):
                res.append(temp[::])
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    temp.append(s[i:j+1])
                    dfs(j + 1)
                    temp.pop()

        dfs(0)
        return res
        
    def isPalindrome(self, s, l, r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True