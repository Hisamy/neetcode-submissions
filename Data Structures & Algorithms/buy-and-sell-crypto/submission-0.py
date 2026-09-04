class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxBenefit = 0 
        slow, fast = 0, 1

        while fast < len(prices):
            if prices[slow] > prices[fast]:
                slow += 1
                if slow == fast:
                    fast += 1
            else:
                benefit = prices[fast] - prices[slow]
                maxBenefit = max(benefit, maxBenefit)
                fast += 1
        return maxBenefit
                

                