class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)[2:]
        x=''
        for i in b:
            if(i=='0'):
                x+='1'
            else:
                x+='0'
        return int(x,2)
