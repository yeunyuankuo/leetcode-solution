def isPalindrome(self, s: str) -> bool:
    # time: O(N)
    # space: O(N)
    clean = ''
    for a in s:
        if a.isalpha() or a.isdigit():
            clean += a.lower()
    return clean == clean[::-1]