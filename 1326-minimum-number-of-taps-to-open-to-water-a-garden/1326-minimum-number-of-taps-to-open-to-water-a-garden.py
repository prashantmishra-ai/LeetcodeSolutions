class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [(max(0, i - ranges[i]), min(n, i + ranges[i])) for i in range(n + 1)]
        intervals.sort(key=lambda x: x[0])

        taps = 0
        i = 0
        start, end = 0, 0

        while start < n:
            while i < n + 1 and intervals[i][0] <= start:
                end = max(end, intervals[i][1])
                i += 1

            if start == end:
                return -1

            taps += 1
            start = end

        return taps
