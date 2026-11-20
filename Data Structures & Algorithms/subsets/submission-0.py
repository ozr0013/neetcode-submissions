class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):           # made a choice for every number
                res.append(subset.copy())
                return
            subset.append(nums[i])       # choice 1: include nums[i]
            dfs(i + 1)
            subset.pop()                 # undo it (backtrack)
            dfs(i + 1)                   # choice 2: skip nums[i]

        dfs(0)
        return res