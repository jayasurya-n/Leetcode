from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def clearStars(self, s: str) -> str:
        # if(s.count('*')==0):return s
        # n = len(s)
        # pq = []
        # for i in range(n):
        #     if(s[i]!='*'):heapq.heappush(pq,(s[i],-i))
        #     elif(pq):heapq.heappop(pq)
        
        # hash = set()
        # while pq:
        #     _,ind = heapq.heappop(pq)
        #     hash.add(-ind)
        
        # ans = []
        # for i in range(n):
        #     if(i in hash):ans.append(s[i])
        # return "".join(ans)

        if(s.count('*')==0):return s
        n = len(s)
        stack = [[] for _ in range(26)]

        ans = list(s)
        for i in range(n):
            if(s[i]!='*'):
                stack[ord(s[i])-97].append(i)
            else:
                for j in range(26):
                    if(stack[j]):
                        ind = stack[j].pop()
                        ans[ind] = '*'
                        break
        return "".join([ch for ch in ans if ch!='*'])

# time complexity: O(nlogn),O(n+26)
# space complexity: O(n),O(26)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))