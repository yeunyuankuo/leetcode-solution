def isAnagram(self, s: str, t: str) -> bool:
    # time: O(N)
    # space: O(128)
    if len(s) != len(t):
        return False
    exist = [0] * 128
    for char in s:
        exist[ord(char)] += 1
    for char in t:
        exist[ord(char)] -= 1
        if exist[ord(char)] < 0:
            return False
    return True