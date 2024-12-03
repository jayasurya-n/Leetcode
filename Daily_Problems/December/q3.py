from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        ans = []
        for i,ch in enumerate(s):
            if(j<len(spaces) and spaces[j]==i):
                ans.append(" ")
                j+=1
            ans.append(ch)
        return "".join(ans)

# time complexity: O(n+m)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))