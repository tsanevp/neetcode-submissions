class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        res = [1] * n

        temp = nums[0]
        # left -> right pass
        for i in range(1, n):
            res[i] = temp
            temp *= nums[i]
        
        temp = nums[-1]
        # right -> left pass
        for i in range(n - 2, -1, -1):
            res[i] *= temp
            temp *= nums[i]

        return res