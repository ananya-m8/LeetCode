class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m=len(nums1)
        n=len(nums2)
        if m<n:
            nums1,nums2=nums2,nums1
        res=[]
        for i in nums2:
            if i in nums1 and i not in res:
                res.append(i)
        return res
