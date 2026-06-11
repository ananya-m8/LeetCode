class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.paren("",res,0,0,n)
        return res
    def paren(self,cur,res,open,close,n):
        if len(cur)==2*n:
            res.append(cur)
            return
        if(open<n):
            self.paren(cur+"(",res,open+1,close,n)
        if close<open:
            self.paren(cur+")",res,open,close+1,n)
