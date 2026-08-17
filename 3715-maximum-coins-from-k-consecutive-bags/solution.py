class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()

        n = len(coins)
        ans = 0

        # Prefix sum of complete intervals
        prefix = [0] * (n + 1)

        for i in range(n):
            l, r, c = coins[i]
            prefix[i + 1] = prefix[i] + (r - l + 1) * c

        # Case 1:
        # Window starts at coins[i][0]
        j = 0

        for i in range(n):
            l, r, c = coins[i]
            end = l + k - 1

            while j < n and coins[j][1] <= end:
                j += 1

            total = prefix[j] - prefix[i]

            # Partial contribution from interval j
            if j < n and coins[j][0] <= end:
                total += (end - coins[j][0] + 1) * coins[j][2]

            ans = max(ans, total)

        # Case 2:
        # Window ends at coins[i][1]
        j = 0

        for i in range(n):
            l, r, c = coins[i]
            start = r - k + 1

            while j <= i and coins[j][1] < start:
                j += 1

            total = prefix[i + 1] - prefix[j]

            # Partial contribution from interval j
            if j <= i and coins[j][0] < start:
                total -= (start - coins[j][0]) * coins[j][2]

            ans = max(ans, total)

        return ans
