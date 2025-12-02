class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums==[]):
            return 0
        nums = sorted(list(set(nums)))
        j=[]
        m=0
        count=1
        for i in range(1,len(nums)):
            j.append(nums[i]-nums[i-1])
            print(j[i-1])
            if(j[i-1]!=1):
                if(m<count):
                    m=count
                    print(m)
                count=1
            else:
                count+=1
        if(m<count):
            m=count
        return m
