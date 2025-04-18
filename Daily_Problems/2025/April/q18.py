from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countAndSay(self, n: int) -> str:
        curr = ['1']
        for _ in range(n-1):
            new = []
            cnt = 1
            for i in range(len(curr)-1):
                if(curr[i]==curr[i+1]):cnt+=1
                else:
                    new.append(str(cnt))
                    new.append(curr[i])
                    cnt = 1
            new.append(str(cnt))
            new.append(curr[-1])
            curr = new
        return "".join(curr)

# time complexity: O(n*m)
# space complexity: O(m)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))