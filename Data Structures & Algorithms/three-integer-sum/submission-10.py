class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        if not nums:
            return res
        
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            self.twoSum(nums, i, res)

        return res
    
    def twoSum(self, nums, i, res):
        left, right = i + 1, len(nums) - 1

        while left < right:
            curr = nums[i] + nums[left] + nums[right]

            if curr == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif curr < 0:
                left += 1
            else:
                right -= 1
