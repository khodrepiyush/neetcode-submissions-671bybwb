class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min1=prices[0]
        for i in prices[1:]:
            if i>min1:
                profit=max(profit,i-min1)
            else:
                min1=min(min1,i)
        return profit
