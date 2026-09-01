class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        rightmax=[0]*n
        maxi=0
        res=0
        for i in range (len(prices)-2,-1,-1):
            maxi = max(maxi,prices[i+1])
            rightmax[i]=maxi
        for i in range(0,len(prices)-1):
            if prices[i] < rightmax[i]:
                res=max(res,rightmax[i]-prices[i])
        return res