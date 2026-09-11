class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        need = len(s1)
        have = 0
        l = 0
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)

        for r in range(len(s2)):
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
            if count1.get(s2[i], 0) < count2[s2[i]]:
                break
            if count1.get(s2[i], 0) == count2[s2[i]]:
                have += 1
            if need == have:
                return True
            
        return False


        
        