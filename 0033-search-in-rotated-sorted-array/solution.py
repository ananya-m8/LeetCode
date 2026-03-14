class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            s = nums[mid]
            if(s==target):
                return mid
            elif(s>=nums[left]):
                if(target>=nums[left] and target<s):
                    right = mid-1
                else:
                    left=mid+1
            else:
                if(target<=nums[right] and target>s):
                    left=mid+1
                else:
                    right=mid-1
        return -1
