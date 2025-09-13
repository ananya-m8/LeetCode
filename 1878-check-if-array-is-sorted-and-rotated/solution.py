class Solution:
    def check(self, nums: List[int]) -> bool:
            n = len(nums)
            if(n<=1):
                return True
            inv=0
            for i in range(1,n):
                if(nums[i]<nums[i-1]):
                    inv+=1
                    if(inv>1):
                        return False
            if(nums[0]<nums[-1]):
                inv+=1
            if(inv<=1):
                return True
            else:
                return False
