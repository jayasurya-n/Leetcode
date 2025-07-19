from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=len)
        hash = set()
        ans = []
        for path in folder:
            ok = True
            s  = ''
            for name in path.split('/'):
                if(name==''):continue
                s+='/'+name
                if(s in hash):
                    ok = False
                    break
            
            if(ok):ans.append(path)
            hash.add(path)
        
        return ans  

# time complexity: O(nlogn+n*k)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))