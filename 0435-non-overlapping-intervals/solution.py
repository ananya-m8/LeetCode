class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=0
        n=len(intervals)
        prev=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<prev:
                count+=1
            else:
                prev=intervals[i][1]
        return count
