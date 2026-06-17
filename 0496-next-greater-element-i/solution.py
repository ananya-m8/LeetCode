class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        stack=[]
        d={}
        for i in range(n-1,-1,-1):
            cur=nums2[i]
            while stack and stack[-1]<=cur:
                stack.pop()
            if not stack:
                d[cur]=-1
            else:
                d[cur]=stack[-1]
            stack.append(nums2[i])
        return [d[i] for i in nums1]
