class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        def helper(listNums):
            oneBack, twoBack = 0, 0
            for i in range(len(listNums)):
                temp = max(listNums[i] + twoBack, oneBack)
                twoBack = oneBack
                oneBack = temp
        
            return oneBack

        return max(helper(nums[1:]), helper(nums[:-1]))

