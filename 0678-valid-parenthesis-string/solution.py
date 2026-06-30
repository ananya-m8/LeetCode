class Solution:
    def checkValidString(self, s: str) -> bool:
        mo,mxo=0,0
        for i in s:
            if i=='(':
                mo+=1
                mxo+=1
            elif i==')':
                mo-=1
                mxo-=1
            else:
                mo-=1
                mxo+=1
            if mxo<0:
                return False
            if mo<0:
                mo=0
        return mo==0
