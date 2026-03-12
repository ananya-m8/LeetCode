class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m+n+1
        d={}
        nums2=nums2+nums1[0:m]
        for i in range(l-1):
            d[nums2[i]]=d.get(nums2[i],0)+1
        k=list(d.keys())
        k.sort()
        for i in range(1,len(k)):

            d[k[i]]+=d[k[i-1]]

        for i in range(-1,-l,-1):
            nums1[d[nums2[i]]-1] = nums2[i]
            d[nums2[i]]-=1
