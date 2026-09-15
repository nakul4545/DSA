class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def fun(stage):
            ans.append(path.copy())
            for i in range(stage, len(nums)):
                path.append(nums[i])
                fun(i + 1)
                path.pop()
        ans = []
        path = []
        fun(0)
        return ans 
