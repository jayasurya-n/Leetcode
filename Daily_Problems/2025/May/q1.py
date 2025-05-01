from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m,n = len(tasks),len(workers)
        tasks.sort()
        workers.sort(reverse=True)
        
        def check(k):
            # k weaker tasks to k stronger workers
            q = deque([])
            cnt = j = 0
            for t in reversed(tasks[:k]):
                while j<k and workers[j]+strength>=t:
                    q.append(workers[j])
                    j+=1
                
                if(not q):return False
                if(q[0]>=t):q.popleft()
                else:
                    if(cnt>=pills):return False
                    cnt+=1
                    q.pop()
            return True
        
        
        low,high = 0,min(m,n)
        while(low<=high):
            mid = (low+high)>>1
            if(not check(mid)):high = mid-1
            else:low = mid+1
        return high

# time complexity: O(nlogn+mlogm+min(m,n)*log(min(m,n)))
# space complexity: O(min(m,n))
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))