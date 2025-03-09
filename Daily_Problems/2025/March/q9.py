from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # n = len(colors)
        # ans = cnt = 0
        # i = j = 0
        # while(j<2*n-1 and i<n):
        #     if(colors[j%n]!=colors[(j+1)%n]):cnt+=1
            
        #     while(i<j and j-i+1>k-1):
        #         if(colors[i%n]!=colors[(i+1)%n]):cnt-=1
        #         i+=1
            
        #     if(i<n and j-i+1==k-1 and cnt==k-1):ans+=1
            
        #     j+=1
            
        # return ans

        n = len(colors)
        ans = 0
        i = j = 0
        while(j<2*n-1 and i<n):
            if(colors[j%n]==colors[(j+1)%n]):
                cnt = 0
                i = j = j+1
                continue
            
            while(i<j and j-i+1>k-1):i+=1
            
            if(i<n and j-i+1==k-1):ans+=1
            
            j+=1
            
        return ans

# time complexity: O(n+k),O(n+k)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))