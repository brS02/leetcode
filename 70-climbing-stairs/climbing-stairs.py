class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        prev2 = 2
        for i in range(n-2):
            cur = prev + prev2
            prev, prev2 = prev2, cur
        return prev2