mod=10**9+7
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even=(n+1)//2
        odd=n//2
        return (self.chakra(5,even)*self.chakra(4,odd))%mod
    def chakra(self,base,power):
        res=1
        base%=mod
        while power>0:
            if power%2==1:
                res=(res*base)%mod
            base=(base*base)%mod
            power//=2
        return res
