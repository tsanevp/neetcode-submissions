class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for ind, val in enumerate(nums):
            temp = target - val

            if temp in seen:
                return [seen[temp], ind]
            
            seen[val] = ind
        
