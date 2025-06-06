from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        s = list(s)
        suffix_smallest = [None]*n
        suffix_smallest[n-1] = n-1
        for i in range(n-2,-1,-1):
            suffix_smallest[i] = suffix_smallest[i+1]
            if(s[i]<=s[suffix_smallest[i+1]]):
                suffix_smallest[i] = i
        
        ds = deque(s)
        ind = 0
        ans = []
        t = []
        while (ds or t):
            t_small = t[-1] if t else '{'
            s_small = s[suffix_smallest[ind]] if ds else '{'

            if(t_small<=s_small):
                ans.append(t.pop())
            else:
                next_ind = suffix_smallest[ind] 
                while(len(ds)>n-next_ind-1):
                    t.append(ds.popleft())
                ind = next_ind+1
        
        return "".join(ans)
    
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        s = si()
        print(Solution().robotWithString(s))