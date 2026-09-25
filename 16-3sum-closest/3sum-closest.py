class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) ==3:
            return sum(nums)
        # Best ans would be sum(i,left,right) == target 
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(closest_sum - target)

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = abs(curr_sum - target)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = curr_sum

                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum