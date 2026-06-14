class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        nums=[]
        self.recur(n,1,nums,k,ans)
        return ans
    def recur(self,sum,ind,nums,k,ans):
        if sum==0 and len(nums)==k:
            ans.append(list(nums))
            return
        if sum<=0 or len(nums)>k:
            return
        for i in range(ind,10):
            if i<=sum:
                nums.append(i)
                self.recur(sum-i,i+1,nums,k,ans)
                nums.pop()
            else:
                break
