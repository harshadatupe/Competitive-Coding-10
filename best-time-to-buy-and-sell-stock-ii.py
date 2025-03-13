class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy
        # tc O(n), sc O(1).
        maxprofit = 0
        for idx in range(len(prices)-1):
            if prices[idx] < prices[idx+1]:
                maxprofit += prices[idx+1] - prices[idx]
        
        return maxprofit