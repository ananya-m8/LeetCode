class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while(left<=right):
            curr=abs(right-left)*min(height[left],height[right])
            if curr>max_area:
                max_area=curr
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_area
