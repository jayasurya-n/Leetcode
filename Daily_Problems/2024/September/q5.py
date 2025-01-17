from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        diff = (n+len(rolls))*mean - sum(rolls)
        if(diff<n or diff>6*n):return []
        ans=[diff//n]*n
        rem = diff%n
        for i in range(rem):ans[i]+=1
        return ans
        
# time complexity: O(max(m,n))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))