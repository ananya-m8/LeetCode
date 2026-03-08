class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
            n = len(nums)
            dg=len(nums[0])
            l = [0]*(2**dg)
            for i in range(n):
                a=int(nums[i],2)
                l[a]=1
            for i in range(2**dg):
                if l[i]==0:
                    binary=bin(i)[2:]

                    if(len(binary)!=dg):
                        binary='0'*(dg-len(binary))+binary
                    return binary
