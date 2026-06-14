
class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        if not digits:
            return ans
        map=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.recur(digits,ans,"",0,map)
        return ans
    def recur(self,digits,ans,s,ind,map):
        if ind==len(digits):
            ans.append(s)
            return
        string=map[int(digits[ind])]
        for char in string:
            self.recur(digits,ans,s+char,ind+1,map)

