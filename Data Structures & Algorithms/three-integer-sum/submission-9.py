class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        if not nums:
            return res
        
        nums.sort()

        ind = 0
        while ind <= len(nums) - 3:
            if nums[ind] > 0:
                break
            
            self.twoSum(ind, nums, res)
            ind += 1
            while ind <= len(nums) - 3 and nums[ind] == nums[ind - 1]:
                ind += 1

        return res
    
    def twoSum(self, i, nums, res):
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
