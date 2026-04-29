class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1 

        for num in nums:
            temp = curMax * num
            curMax = max(temp,num*curMin,num)
            curMin = min(temp,num*curMin,num)
            res = max(res,curMax)
        return res