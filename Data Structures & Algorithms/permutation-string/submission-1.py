class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # bf :
        if len(s1) > len(s2):
            return False
        s1 = sorted(s1)
        l = 0
        r = len(s1)
        while r <= len(s2):
            s22 = s2[l:r]
            s22 = sorted(s22)
            if s22 == s1:
                return True
            l += 1
            r += 1
        return False
