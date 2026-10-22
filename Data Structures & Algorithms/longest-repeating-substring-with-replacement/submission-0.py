class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxcount = 0
        res = 0
        l = 0
        n = len(s)

        for i in range(n):
            count[s[i]] = count.get(s[i],0) + 1
            maxcount = max(maxcount,count[s[i]])

            if (i - l + 1) - maxcount > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res,i - l + 1)
        return res
