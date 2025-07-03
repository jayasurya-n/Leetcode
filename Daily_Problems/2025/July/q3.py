from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def kthCharacter(self, k: int) -> str:
        # ans = ['a']
        # while len(ans)<k:
        #     n = len(ans)
        #     for i in range(n):
        #         inc = (ord(ans[i])-97+1)%26
        #         ans.append(chr(97+inc))
        # return ans[k-1]

        length = 1
        while length<k:length<<=1

        shifts = 0
        while length>1:
            half = length>>1
            if(k>half):
                shifts=(1+shifts)%26
                k-=half
            length = half
        
        return (chr(97+shifts))

# time complexity: O(k),O(logk)
# space complexity: O(k),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))