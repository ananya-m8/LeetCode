class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and stack[-1]>i and k>0:
                k-=1
                stack.pop()
            stack.append(i)
        while stack and k>0:
            stack.pop()
            k-=1
        while(stack and stack[0]=='0'):
            stack.pop(0)
        s=''.join(stack)
        return s or '0'
