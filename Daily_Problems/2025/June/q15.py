from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxDiff(self, num: int) -> int:
        s1 = list(str(num))
        s2 = s1[:]
        n = len(s1)

        i = 0
        while i<n and s1[i]=='9':i+=1

        maxi = mini = num
        if(i<n):
            ch = s1[i]
            for j in range(i,n):
                if(s1[j]==ch):
                    s1[j] = '9'

            maxi = int("".join(s1))
        
        bool = all(s2[0]==ch for ch in s2) 
        
        if(bool):s2 = ['1']*n
        elif(s2[0]!='1'):
            ch = s2[0]
            for j in range(0,n):
                if(s2[j]==ch):
                    s2[j] = '1'
        else:
            i = 0
            while i<n and (s2[i]=='1' or s2[i]=='0'):i+=1
            if(i<n):
                ch = s2[i]
                for j in range(i,n):
                    if(s2[j]==ch):
                        s2[j] = '0'
        
        mini = int("".join(s2))
        return maxi-mini
    
# time complexity: O(logn)
# space complexity: O(logn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))