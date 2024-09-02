from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        k%=sum(chalk)
        i = 0
        while(k>=0):
            k-=chalk[i]
            if(k<0):return i
            i+=1

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        chalk = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().chalkReplacer(chalk,k))