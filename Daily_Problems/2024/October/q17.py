from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def maximumSwap(self, num: int) -> int:
    #     if(num<10):return num
    #     digits = []
    #     temp = num
    #     while(temp):
    #         digits.append(temp%10)
    #         temp//=10
        
    #     ans = num
    #     n = len(digits)
    #     digits.reverse()
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             ans = max(ans,num+(digits[j]-digits[i])*(10**(n-i-1))
    #                       +(digits[i]-digits[j])*(10**(n-j-1)))
    #     return ans
    
    def maximumSwap(self, num: int) -> int:
        if(num<10):return num
        digits = []
        temp = num
        while(temp):
            digits.append(temp%10)
            temp//=10
        
        digits.reverse()
        n = len(digits)
        maxRight = [0]*n
        maxi = n-1
        maxRight[n-1] = maxi
        for i in range(n-2,-1,-1):
            if(digits[i]>digits[maxi]):maxi = i
            maxRight[i] = maxi
        
        print(digits)
        print(maxRight)
        for i in range(n):
            j = maxRight[i]
            if(digits[j]>digits[i]):
                return num+(digits[j]-digits[i])*(10**(n-i-1))+(digits[i]-digits[j])*(10**(n-j-1))
        return num
    
# time complexity: O((logn)^2),O(logn)
# space complexity: O(logn),O(logn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        print(Solution().maximumSwap(n))