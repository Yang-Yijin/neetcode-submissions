class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = []
        s = s.lower()
        for x in s:
            if (x >= 'a' and x <= 'z') or (x >= '0' and x <= '9'):
                n.append(x)
        l = 0
        r = len(n)-1
        #print(r)
        while l < r:
            if n[l] != n[r]:
                return False
            l += 1
            r -= 1
        return True