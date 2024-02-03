import collections

class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # time: O(1)
        # space: O(N)
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # time: O(logN)
        # space: O(1)
        res = ""
        timestampVals = self.store[key]

        l, r = 0, len(timestampVals) - 1
        while l <= r:
            mid = (l + r) // 2
            val = timestampVals[mid][0]
            time = timestampVals[mid][1]

            if time <= timestamp:
                res = val
                l = mid + 1
            else:
                r = mid - 1

        return res