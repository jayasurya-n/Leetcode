from typing import List, Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int, input().strip().split()))


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        valid = []
        for mask in range(3**m):
            ok = True
            col = []
            for i in range(m):
                col.append(mask % 3)
                mask //= 3
                if i > 0 and col[i] == col[i - 1]:
                    ok = False
                    break
            if ok:valid.append(col)

        p = len(valid)
        adj = [[] for _ in range(p)]

        for i in range(p):
            for j in range(p):
                if i == j:continue
                ok = True
                for k in range(m):
                    if valid[i][k] == valid[j][k]:
                        ok = False
                        break
                if ok:adj[i].append(j)

        prev = [1] * p
        for i in range(1, n):
            curr = [0] * p
            for j in range(p):
                for k in adj[j]:
                    curr[j] = (curr[j] + prev[k]) % mod
            prev = curr
        
        return sum(prev)%mod

# time complexity: O(m(3**m)+p^2*m+p^2*n)
# space complexity: O(3mn)
if __name__ == "__main__":
    for _ in range(ii()):
        m, n = lii()
        print(Solution().colorTheGrid(m, n))
