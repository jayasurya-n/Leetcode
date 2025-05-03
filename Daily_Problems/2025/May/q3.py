from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        def check(x):
            cnt1 = cnt2 = 0
            for i in range(n):
                a,b = tops[i],bottoms[i]
                if(a!=x and b!=x):return -1
                if(a!=x):cnt1+=1
                elif(b!=x):cnt2+=1
            return min(cnt1,cnt2)
        
        ans1 = check(tops[0]) 
        ans2 = check(bottoms[0])
        if(ans1==-1 and ans2==-1):return -1
        if(ans1!=-1 and ans2!=-1):return min(ans1,ans2)
        return max(ans1,ans2)
         
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))