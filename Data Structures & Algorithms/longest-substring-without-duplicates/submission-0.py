class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        res = 0
        for i in s:
            while i in arr:
                arr.pop(0)
            arr.append(i)
            res = max(res,len(arr))
        return res