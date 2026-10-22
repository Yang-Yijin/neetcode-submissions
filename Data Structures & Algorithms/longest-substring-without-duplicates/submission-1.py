class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # arr = []
        # res = 0
        # for i in s:
        #     while i in arr:
        #         arr.pop(0)
        #     arr.append(i)
        #     res = max(res,len(arr))
        # return res
        flag = set()
        res = 0
        n = len(s)
        l = 0
        for r in range(n):
            while s[r] in flag:
                flag.remove(s[l])
                l += 1
            flag.add(s[r])
            res = max(res,len(flag))
        return res