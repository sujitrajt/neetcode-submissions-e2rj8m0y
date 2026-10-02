class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climbHelper(i):
            if i <= 1:
                return 1
            
            if i in memo:
                return memo[i]
            
            memo[i] = climbHelper(i-1) + climbHelper(i-2)
            return memo[i]
        return climbHelper(n)