class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(rem,comb,start):
            if rem==0:
                res.append(list(comb))
                return
            if rem<0:
                return
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                backtrack(rem-candidates[i],comb,i)
                comb.pop()
        res=[]
        backtrack(target,[],0)
        return res
