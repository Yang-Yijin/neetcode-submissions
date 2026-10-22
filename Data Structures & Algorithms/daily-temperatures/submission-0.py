class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = []
        for i in range(len(t)):
            flag = 0
            for j in range(i+1,len(t)):
                if t[j] > t[i]:
                    res.append(j-i)
                    flag = 1
                    break
            if flag == 0:
                res.append(0)
        return res