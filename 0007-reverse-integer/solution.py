class Solution:
    def reverse(self, x: int) -> int:
        sign=+1
        if x<0:
            sign=-1
            x*=sign
        x=sign*int(str(x)[::-1])
        return x if -2**31<=x<=2**31+1 else 0
