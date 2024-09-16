from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = sys.maxsize
        for i in range(len(timePoints)-1):
            h1,m1 = map(int,timePoints[i].split(":"))
            h2,m2 = map(int,timePoints[i+1].split(":"))
            ans = min(ans,(h2-h1)*60+(m2-m1))
        
            h1,m1 = map(int,timePoints[-1].split(":"))
            h2,m2 = map(int,timePoints[0].split(":"))
        ans = min(ans,(24+h2-h1)*60+(m2-m1))
        return ans
            
# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        timePoints = input().strip().split()
        print(Solution().findMinDifference(timePoints))