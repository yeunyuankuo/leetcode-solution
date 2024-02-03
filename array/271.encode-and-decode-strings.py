class Codec:
    def encode(self, strs: list[str]) -> str:
        # time: O(N)
        # spcae: O(1)
        """Encodes a list of strings to a single string.
        """
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        # time: O(N)
        # space: O(N)
        l, r = 0, 0
        ans = []
        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])
                r += 1
                ans.append(s[r:(r + length)])
                r = r + length
                l = r
            else:
                r += 1
        return ans