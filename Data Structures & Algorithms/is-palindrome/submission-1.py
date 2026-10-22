class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        s = s.lower()
        for a in s:
            if 'a' <= a <= 'z' or '0' <= a <= '9':
                chars.append(a)
        l = 0
        r = len(chars) - 1
        while l < r:
            if chars[l] != chars[r]:
                return False
            l += 1
            r -= 1
        return True 