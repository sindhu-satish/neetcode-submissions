class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        need = len(t)
        countt = {}
        counts = {}
        res = [-1, -1]
        res_len = float(inf)
        for c in t:
            countt[c] = countt.get(c, 0) + 1

        l, r = 0, 0

        for r in range(len(s)):
            counts[r] = counts.get(s[r], 0) + 1

            if s[r] in countt and countt[s[r]] == counts[s[r]]:
                have += 1

                

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    res_len = min(r - l + 1, res_len)
                if s[l] in countt and countt[s[l]] < counts[s[l]]: 
                    have -= 1
                counts[l] -= 1
                l += 1
        l, r = res

        return s[l : r + 1] if resLen != float("infinity") else ""

            

            


        