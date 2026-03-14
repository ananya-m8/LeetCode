class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            s=nums[mid]
            if(s==target):
                return True
            elif(s==nums[left]):
                left+=1
                continue
            if(nums[left]<=s):
                if(nums[left]<=target<=s):
                    right=mid-1
                else:
                    left=mid+1
            else:
                if(s<=target<=nums[right]):
                    left=mid+1
                else:
                    right=mid-1
        return False
