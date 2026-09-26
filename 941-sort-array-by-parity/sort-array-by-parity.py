class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        low = 0 
        high= len(nums) - 1
        if len(nums) == 1:
            return nums
        while low < high:
            if nums[low] %2 == 0 and nums[high] %2 == 0:
                low += 1
            elif nums[high] %2 == 0:
                nums[low], nums[high] = nums[high], nums[low]
                high -= 1
                low += 1
            else:
                high -= 1
        return nums