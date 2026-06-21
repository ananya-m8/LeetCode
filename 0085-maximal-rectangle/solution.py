class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Return 0 if matrix is empty
        if not matrix: return 0

        # Get column count
        m = len(matrix[0])

        # Initialize histogram
        height = [0] * m
        max_area = 0

        # Traverse each row
        for row in matrix:

            # Update histogram
            for i in range(m):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0

            # Update max area
            max_area = max(max_area, self.largestRectangleArea(height))

        return max_area
    def largestRectangleArea(self, heights):

        # Add a sentinel bar
        heights.append(0)

        # Stack for indices
        stack = []
        max_area = 0

        # Traverse through histogram bars
        for i in range(len(heights)):

            # Pop and calculate while current is smaller
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            # Push current index
            stack.append(i)

        return max_area
