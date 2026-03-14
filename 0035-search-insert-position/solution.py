class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            t=nums[mid]
            if(t==target):
                return mid
            elif(t>target):
                right=mid-1
            else:
                left=mid+1
        return left
            
