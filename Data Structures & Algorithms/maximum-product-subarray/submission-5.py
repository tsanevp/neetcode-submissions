class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for i in range(len(nums)):
            temp = nums[i] * currMax
            currMax = max(temp, nums[i] * currMin, nums[i])
            currMin = min(temp, nums[i] * currMin, nums[i])
            res = max(res, currMin, currMax, nums[i])
        return res