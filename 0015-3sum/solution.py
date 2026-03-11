class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        l=[]
        nums.sort()
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            left=i+1
            right=n-1
            while(left<right):
                s=nums[i]+nums[right]+nums[left]
                if(s>0):
                    right-=1
                elif(s<0):
                    left+=1
                else:
                    l.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return l
