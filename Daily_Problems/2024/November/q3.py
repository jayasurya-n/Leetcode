from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)!=len(goal)):return False
        # for _ in range(len(s)):
        #     if(s==goal):return True
        #     s = s[1:]+s[0]
        # return False
        ns = s+s
        return ns.find(goal)!=-1
    
# time complexity: O(n^2),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))