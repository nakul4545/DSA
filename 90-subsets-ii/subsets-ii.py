class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        path = []
        def backtrack(stage):
            ans.append(path.copy())

            for i in range(stage,len(nums)):
                if i > stage and nums[i] == nums[i - 1]:
                    continue 
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return ans
                