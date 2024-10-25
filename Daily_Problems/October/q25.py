from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        for i in range(1,len(folder)):
            lastFolder = result[-1]
            lastFolder+="/"
            if not folder[i].startswith(lastFolder):result.append(folder[i])
        return result

# time complexity: O(nlogn*l)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))