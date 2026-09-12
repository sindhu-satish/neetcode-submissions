class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        cur_subset = []
        subsets = []

        def backtrack(start):
            subsets.append(cur_subset.copy())

            for i in range(start, len(nums)):
                # skip duplicate choices at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                cur_subset.append(nums[i])
                backtrack(i + 1)
                cur_subset.pop()

        backtrack(0)

        return subsets