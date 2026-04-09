class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        twoBack, oneBack = 0, 0
        for i in range(len(nums)):
            nums[i] = max(nums[i] + twoBack, oneBack)
            twoBack = oneBack
            oneBack = nums[i]
        
        return nums[-1]