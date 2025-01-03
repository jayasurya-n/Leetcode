from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # n = len(prices)
        # nse = [-1]*n
        # stack = []
        # for i in range(n-1,-1,-1):
        #     while(stack and stack[-1]>prices[i]):stack.pop()
        #     if(stack):nse[i] = stack[-1]
        #     stack.append(prices[i])
        
        # return [prices[i]-nse[i] if nse[i]!=-1 else prices[i] for i in range(n)]
        
        stack = []
        for i in range(len(prices)):
            while(stack and prices[stack[-1]]>=prices[i]):
                prices[stack.pop()]-=prices[i]
            stack.append(i)
        return prices
            
# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))