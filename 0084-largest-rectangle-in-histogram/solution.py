class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # Treat height as 0 when i == n (imaginary bar)
            current_height = heights[i] if i < n else 0

            while stack and (i == n or heights[stack[-1]] >= current_height):
                height = heights[stack.pop()]  #pop from the stack

                if not stack:
                    width = i  #take width as i if not in stack else i-stack[-1]-1
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)  #calculate the max area 

            stack.append(i)

        return max_area #return the max area
