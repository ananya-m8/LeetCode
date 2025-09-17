import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if(i not in d and nums.count(i)>math.floor(len(nums)/2)):
                return i
            else:
                d[i] = 1
