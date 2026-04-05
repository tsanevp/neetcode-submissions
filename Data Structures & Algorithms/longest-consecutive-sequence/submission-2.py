class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        if not nums:
            return res

        seen = set(nums)
        for num in seen:
            if num + 1 not in seen:
                temp = 1
                while num - temp in seen:
                    temp += 1
                
                res = max(res, temp)

        return res
