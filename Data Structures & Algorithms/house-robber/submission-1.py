class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = {}
        def robHelper(i):
            if i == 0:
                return 0
            if i == 1:
                return nums[0]
            if i in memo:
                return memo[i]

            skip = robHelper(i-1)
            take = robHelper(i-2) + nums[i-1]
            memo[i] = max(skip,take)
            return memo[i]
        return robHelper(len(nums))