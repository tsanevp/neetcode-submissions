class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            curr = target - num

            if curr in seen:
                return [seen[curr], i]
            
            seen[num] = i
        
        return [0, 1]