class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        twoBack, oneBack = 0, 0
        for i in range(len(nums)):
            temp = max(nums[i] + twoBack, oneBack)
            twoBack = oneBack
            oneBack = temp
        
        return oneBack