class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=0
        for i in range(left,right+1):
            x=bin(i)[2:].count('1')
            if(x not in (0,1)):
                for j in range(2,x//2+1):
                    if x%j==0:
                        break
                else:
                    c+=1
        return c
