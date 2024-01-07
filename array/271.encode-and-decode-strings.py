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
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res