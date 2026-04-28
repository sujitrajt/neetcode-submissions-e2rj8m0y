class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedInterval = sorted(intervals,key=lambda x : x[0])
        mergedInterval = []

        for interval in sortedInterval:
            if not mergedInterval or  interval[0] > mergedInterval[-1][1]:
                mergedInterval.append(interval)
            else:
                mergedInterval[-1][1] = max(interval[1],mergedInterval[-1][1])
        return mergedInterval