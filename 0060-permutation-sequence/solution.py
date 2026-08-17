class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[str(i) for i in range(1,n+1)]
        k-=1
        res=''
        for i in range(n,0,-1):
            fact=math.factorial(i-1)
            index=k//fact
            res+=nums.pop(index)
            k%=fact
        return res
