class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #min_=min(prices)
        max=0
        B_i=0
        S_i=1
        for i in range(len(prices)-1):
            if (prices[S_i]>prices[B_i]):
                if max<prices[S_i]-prices[B_i]:
                    max=prices[S_i]-prices[B_i]
            else:
                B_i=S_i
            S_i=S_i+1
            
        return max