from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pair = 'ab' if x>y else 'ba'
        stack = []
        ans = 0
        for ch in s:
            if(stack and stack[-1]==pair[0] and ch==pair[1]):
                stack.pop()
                ans+=max(x,y)
            else:stack.append(ch)
        
        other_pair = pair[::-1]
        cnt = 0
        for ch in stack:
            if(ch!='b' and ch!='a'):cnt=0
            if(ch==other_pair[0]):cnt+=1
            else:
                if(cnt>0):
                    ans+=min(x,y)
                    cnt-=1
        
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))