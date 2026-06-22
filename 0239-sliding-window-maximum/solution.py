class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        n=len(nums)
        if k==n:
            return [max(nums)]
        dq = deque()
        # Result list to store window maximums
        result = []
        # Loop through each element
        for i in range(n):
            # Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove all elements from the back that are smaller than current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index to deque
            dq.append(i)

            # Append max to result once the first window is completed
            if i >= k - 1:
                result.append(nums[dq[0]])

        # Return the result list
        return result
