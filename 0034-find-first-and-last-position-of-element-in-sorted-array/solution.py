class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            ans=-1
            left = 0
            right=len(nums)-1
            while(left<=right):
                mid=(left+right)//2
                t=nums[mid]
                if(t==target):
                    ans=mid
                    right=mid-1
                elif(t>target):
                   right=mid-1
                else:
                    left=mid+1
            return ans
        def last():
            ans=-1
            left = 0
            right=len(nums)-1
            while(left<=right):
                mid=(left+right)//2
                t=nums[mid]
                if(t==target):
                    ans=mid
                    left=mid+1
                elif(t>target):
                   right=mid-1
                else:
                    left=mid+1
            return ans
        return [first(),last()]
