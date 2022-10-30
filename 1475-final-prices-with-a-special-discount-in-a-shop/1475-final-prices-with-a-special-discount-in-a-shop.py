class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(0,(len(prices)-1)):
            addIndex=1
            while (i+addIndex+1)<len(prices) and prices[i] < prices[i+addIndex]:
                addIndex+=1
            if prices[i] >= prices[i+addIndex]:
                prices[i]=prices[i]-prices[i+addIndex]
        # print(prices)
        return prices
            
            