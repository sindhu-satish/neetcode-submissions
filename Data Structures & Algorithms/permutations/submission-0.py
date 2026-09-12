class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans, sol = [], []

        def backtrack():
            if len(ans) == len(nums):
                sol.append(ans[:])

            for i in range(len(nums)):
                if nums[i] not in ans:
                    ans.append(nums[i])
                    backtrack()
                    ans.pop()

        backtrack()

        return sol


        