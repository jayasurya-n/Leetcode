from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i,j = 0,0
        
        while i<n or j<n:
            while(i<n and start[i]=='_'):i+=1
            while(j<n and target[j]=='_'):j+=1
            
            if(i==n or j==n):return i==j
            if(start[i]!=target[j] or
            (start[i]=='L' and i<j) or 
            (start[i]=='R' and j<i)):return False
            i+=1
            j+=1
        return True                
    
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))