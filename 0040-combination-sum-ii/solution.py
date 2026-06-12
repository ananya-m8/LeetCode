class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort the candidates to handle duplicates
        ans = []  # To store the result
        ds = []  # To store a current combination
        self.findCombination(0, target, candidates, ans, ds)  # Start the recursive search
        return ans  # Return all valid combinations
    def findCombination(self,ind,target,arr,ans,ds):
        if target == 0:
            ans.append(list(ds))  # Add the current combination to the result
            return

        # Loop through the elements starting from index 'ind'
        for i in range(ind, len(arr)):
            # Skip duplicates to avoid repeating combinations
            if i > ind and arr[i] == arr[i - 1]:
                continue

            # If the current element is greater than the remaining target, break the loop
            if arr[i] > target:
                break

            # Include the current element in the combination
            ds.append(arr[i])

            # Recur with the updated target and next index (i + 1 to avoid repetition)
            self.findCombination(i + 1, target - arr[i], arr, ans, ds)

            # Backtrack by removing the last added element
            ds.pop()

