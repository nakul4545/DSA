class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, res, path,curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
            if index == len(candidates) or curr_sum > target:
                return
            path.append(candidates[index])
            backtrack(index, res, path, curr_sum + candidates[index]) #Taking the current index
            path.pop()

            # Not taking the current index 
            backtrack(index+1, res, path, curr_sum)
        res = []
        backtrack(0, res, [], 0)
        return res
        