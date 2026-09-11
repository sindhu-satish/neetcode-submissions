class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > 0:
                    r = r - 1

                elif threeSum < 0:
                    l = l + 1

                else:
                    res.append([nums[i], nums[l],nums[r]])
                    l = l + 1
                    r = r - 1
                    while l < r and nums[l] != nums[l-1]:
                        l += 1
        return res


        