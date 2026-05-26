class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        n=''
        j=1
        if(s!='' and s[0] in '+-'):
            if(s[0]=='-'):
                j=-1
            s=s[1:]
        for i in s:
            if i.isdigit():
                n+=i
            else:
                break
        n=int(n or 0)*j
        low,high=-2**31,2**31-1
        if(n<low):
            return low
        elif(n>high):
            return high
        return n
