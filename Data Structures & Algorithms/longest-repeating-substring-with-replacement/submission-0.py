class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_ = {}
        l = 0
        n = len(s)
        res = 0
        for r in range(n):
            count_[s[r]] = 1 + count_.get([s[r]], 0)
            while r - l + 1 - max(count_.values()) > k:
                count_[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)
        return res
                



        