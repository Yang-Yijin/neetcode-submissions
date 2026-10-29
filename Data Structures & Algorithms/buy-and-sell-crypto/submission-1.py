class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for i in prices:
            min_price = min(i,min_price)
            res =max(res, i - min_price)
        return res
