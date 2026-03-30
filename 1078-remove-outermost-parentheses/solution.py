class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        res=''
        for i in s:
            if(i=='('):
                c+=1
                if(c>1):
                    res+=i
            else:
                c-=1
                if(c>0):
                    res+=i
        return res
