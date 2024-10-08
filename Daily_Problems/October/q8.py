from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = 0
        for ch in s:
            if(ch=='['):cnt+=1
            elif(cnt>0 and ch==']'):cnt-=1
        return (cnt+1)//2
                
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))