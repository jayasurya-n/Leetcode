from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minMaxDifference(self, num: int) -> int:
        # arr = []
        # while num:
        #     arr.append(num%10)
        #     num//=10
        # arr.reverse()
        
        # maxi,mini = 0,10**10
        # for digit1 in range(0,10):
        #     temp = arr[:]
        #     for i,digit2 in enumerate(temp):
        #         if(digit1==digit2):
        #             temp[i] = 9
            
        #     new = 0
        #     for digit2 in temp:
        #         new = new*10+digit2
        #     maxi = max(maxi,new)

        #     temp = arr[:]
        #     for i,digit2 in enumerate(temp):
        #         if(digit1==digit2):
        #             temp[i] = 0
            
        #     new = 0
        #     for digit2 in temp:
        #         new = new*10+digit2
        #     mini = min(mini,new)
        
        # return maxi-mini

        s1 = list(str(num))
        s2 = s1[:]

        i = 0
        while i<len(s1) and s1[i]=='9':i+=1

        maxi = mini = num
        if(i<len(s1)):
            ch = s1[i]
            for j in range(i,len(s1)):
                if(s1[j]==ch):
                    s1[j] = '9'

            maxi = int("".join(s1))
        
        ch = s2[0]
        for j in range(0,len(s2)):
            if(s2[j]==ch):
                s2[j] = '0'
        
        mini = int("".join(s2))

        return maxi-mini
    
# time complexity: O(9logn),O(logn)
# space complexity: O(logn),O(logn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))