class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        
        if not nums:
            return res
        
        if len(nums) == 1:
            return nums[0]
        
        def getProfit(houses):
            if not houses:
                return 0
            
            oneBack, twoBack = 0, 0
            for i in range(len(houses)):
                temp = max(twoBack + houses[i], oneBack)
                twoBack = oneBack
                oneBack = temp                
            
            return oneBack

        return max(getProfit(nums[1:]), getProfit(nums[:-1]))