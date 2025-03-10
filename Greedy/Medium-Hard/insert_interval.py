from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ns,ne = newInterval
        
        ans = []
        i = 0
        while(i<n):
            if(intervals[i][1]<ns):ans.append(intervals[i])
            else:break
            i+=1
        
        while(i<n):
            if(max(intervals[i][0],ns)<=min(intervals[i][1],ne)):
                ns,ne = min(intervals[i][0],ns),max(intervals[i][1],ne)
            else:break
            i+=1
        ans.append([ns,ne])
        
        while(i<n):
            ans.append(intervals[i])
            i+=1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))