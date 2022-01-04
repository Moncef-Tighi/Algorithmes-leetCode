class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice =99999
        i, maxprofit=0, 0
        while i<len(prices):
            if prices[i]<minprice:
                minprice=prices[i]
            elif prices[i]-minprice>maxprofit:
                maxprofit = prices[i] - minprice
            i+=1
        return maxprofit