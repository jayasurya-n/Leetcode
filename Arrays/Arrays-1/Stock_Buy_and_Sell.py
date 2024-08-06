class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max = -1e6
        profit = 0

        start = -1
        stop = -1

        for i in range(0,len(prices)-1):
            if(profit==0):start_i=i
            profit += (prices[i+1]-prices[i])
            if(profit > max):
                max = profit
                start = start_i
                stop = i
            if (profit<0):
                profit = 0

        if(max<0):max = 0
        return max,start,stop
        pass


prices = [int(x) for x in input().strip().split()]
obj = Solution()
print(obj.maxProfit(prices))