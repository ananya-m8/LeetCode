class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        prefix_count={0:1}
        prefix_sum=0
        for i in range(n):
            prefix_sum+=nums[i]
            if prefix_sum-k in prefix_count:
                count+=prefix_count[prefix_sum-k]
            prefix_count[prefix_sum]=prefix_count.get(prefix_sum,0)+1
        return count
