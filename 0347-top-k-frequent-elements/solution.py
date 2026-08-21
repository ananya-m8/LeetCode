class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        heap=[]
        res=[]
        for num,cnt in d.items():
            heapq.heappush(res,(cnt,num))
            if len(res)>k:
                heapq.heappop(res)
        return [val[1] for val in res] 
