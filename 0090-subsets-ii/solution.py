class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        self.backtrack(0,nums,[],res)
        return res
    def backtrack(self,start,nums,cur,res):
        res.append(list(cur))
        for i in range(start,len(nums)):
            if i>start and nums[i] == nums[i - 1]:
                continue

            # Include nums[i]
            cur.append(nums[i])

            # Recurse
            self.backtrack(i + 1, nums, cur, res)

            # Backtrack
            cur.pop()
