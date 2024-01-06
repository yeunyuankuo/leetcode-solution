import collections

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    # time: O(N*M), N is the number of strings in strs, M is the average length of strings inside strs
    # space: O(N*M), N is the number of strings in strs, M is the average length of strings inside strs
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()