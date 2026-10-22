class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        for sh in s:
            countS[sh] = countS.get(sh, 0) + 1
        for th in t:
            countT[th] = countT.get(th, 0) + 1
        return countS == countT