from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # n = len(fruits)
        # psum  = [0]*(n+1)
        # for i in range(1,n+1):
        #     psum[i] = psum[i-1]+fruits[i-1][1]
        
        # fruits_pos = [fruits[i][0] for i in range(n)]
        
        # ans = 0
        # for x in range(0,k//2+1):
        #     y = k-2*x

        #     # left
        #     pos1 = startPos-x
        #     pos2 = startPos+y
        #     ind1 = bisect.bisect_left(fruits_pos,pos1) 
        #     ind2 = bisect.bisect_right(fruits_pos,pos2) 
        #     ans = max(ans,psum[ind2]-psum[ind1])

        #     # right
        #     pos1 = startPos+x
        #     pos2 = startPos-y
        #     ind1 = bisect.bisect_right(fruits_pos,pos1) 
        #     ind2 = bisect.bisect_left(fruits_pos,pos2) 
        #     ans = max(ans,psum[ind1]-psum[ind2])

        # return ans

        n = len(fruits)
        ans = curr = left = 0

        steps = lambda left,right:fruits[right][0]-fruits[left][0]+min(abs(startPos-fruits[left][0]),abs(startPos-fruits[right][0]))
        
        for right in range(n):
            curr+=fruits[right][1]

            while left<=right and steps(left,right)>k:
                curr-=fruits[left][1]
                left+=1
            
            ans = max(ans,curr)
        
        return ans

# time complexity: O(n+klogn),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))