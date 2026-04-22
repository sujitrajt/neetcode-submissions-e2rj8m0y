class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        n = len(intervals)
        i = 0 

        #pharse 1 add all intervals to merged that starts before the new interval and end before it 
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i+=1
        print(merged)
        #pharse 2 merge all interval while overlap with new interval
        # start time should be less than end time of new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i += 1
        merged.append(newInterval)

        #pharse3 add the remaining interval from j to n to merged 
        for j in range(i,n):
            merged.append(intervals[j])
        return merged