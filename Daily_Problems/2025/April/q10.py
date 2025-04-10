from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def findCount(num):
            if(num<int(s)):return 0
            t = str(num)
            diff = len(t)-len(s)
            if(diff==0):return 1
            
            ans = 0          
            for i in range(diff):
                if(limit<int(t[i])):
                    ans+=(limit+1)**(diff-i)
                    return ans
                ans+=int(t[i])*(limit+1)**(diff-i-1)
                
            if(int(t[diff:])>=int(s)):ans+=1
            return ans
        
        return findCount(finish)-findCount(start-1)

# time complexity: O(logn)
# space complexity: O(logn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))