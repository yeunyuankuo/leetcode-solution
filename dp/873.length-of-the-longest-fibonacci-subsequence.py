class Solution:
    # brute force solution
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        res = 0
        size = len(arr)
        for i in range(size):
            for j in range(i+1, size):
                k = j + 1
                curr = 0
                f1 = i
                f2 = j
                while k < size:
                    if arr[f1] + arr[f2] == arr[k]:
                        curr += 1
                        res = max(res, curr)
                        f1 = f2
                        f2 = k
                    k += 1

        if res > 0:
            res += 2
        return res 
    
    # memoization
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        res = 0
        size = len(arr)

        idxmap = dict()
        for idx, value in enumerate(arr):
            idxmap[value] = idx

        for i in range(size):
            for j in range(i+1, size):
                curr = 0
                f1 = i
                f2 = j
                
                while arr[f1] + arr[f2] in idxmap:
                    curr += 1
                    res = max(res, curr)
                    k = idxmap[arr[f1] + arr[f2]]
                    f1 = f2
                    f2 = k

        if res > 0:
            res += 2
        return res 