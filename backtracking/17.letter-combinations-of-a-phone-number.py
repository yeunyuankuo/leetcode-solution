class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # time: O(N * 4^N), N is the length of digits, and 4^N b/c 4 is the max length in the hash map
        # space: O(N), where N is the length of digits
        table = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def bt(i, temp):
            if i >= len(digits):
                res.append(temp)
                return

            for c in table[digits[i]]:
                bt(i + 1, temp + c)

        if digits:
            bt(0, "")

        return res