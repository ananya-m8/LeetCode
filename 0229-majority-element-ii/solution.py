import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = math.floor(len(nums)/3)
        num1=None
        num2=None
        c1=0
        c2=0
        for i in nums:
            if i==num1:
                c1+=1
            elif i==num2:
                c2+=1
            elif c1==0:
                num1=i
                c1=1
            elif c2==0:
                num2=i
                c2=1
            else:
                c1-=1
                c2-=1
        l=[]
        if(num1!=None and nums.count(num1)>n):
            l.append(num1)
        if(num2!=None and nums.count(num2)>n):
            l.append(num2)
        
        return l
