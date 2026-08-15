class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergesort(nums,0,len(nums)-1)
    def mergesort(self,nums,low,high):
        if low>=high:
            return 0
        mid=(low+high)//2
        count=0
        count+=self.mergesort(nums,low,mid)
        count+=self.mergesort(nums,mid+1,high)
        count+=self.rev_pr(nums,low,mid,high)
        self.merge(nums,low,mid,high)
        return count
    def rev_pr(self,nums,low,mid,high):
        count=0
        j=mid+1
        for i in range(low,mid+1):
            while(j<=high and nums[i]>nums[j]*2):
                j+=1
            count+=(j-(mid+1))
        return count
    def merge(self,nums,low,mid,high):
        i=low
        j=mid+1
        temp=[]
        while i<=mid and j<=high:
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i+=1
            else:
                temp.append(nums[j])
                j+=1
        while i<=mid:
            temp.append(nums[i])
            i+=1
        while j<=high:
            temp.append(nums[j])
            j+=1
        for k in range(len(temp)):
            nums[low+k]=temp[k]
