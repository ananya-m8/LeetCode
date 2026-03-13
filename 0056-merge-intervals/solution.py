class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        left=0
        l=[]
        intervals.sort()
        right=0
        n=len(intervals)
        for i in range(1,n):
            if(intervals[i]==intervals[right]):
                continue
            if(intervals[i][0]<=intervals[right][1]):
                if(intervals[i][1]>intervals[right][1]):
                    right=i
            else:
                l.append([intervals[left][0],intervals[right][1]])
                left=i
                right=i
        else:
            l.append([intervals[left][0],intervals[right][1]])
        return l
