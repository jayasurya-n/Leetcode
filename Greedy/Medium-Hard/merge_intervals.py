from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        ps,pe = intervals[0]
        i = 1
        while(i<len(intervals)):
            if(intervals[i][0]>pe):
                ans.append([ps,pe])
                ps,pe = intervals[i]
            else:pe = max(pe,intervals[i][1])
            i+=1
        ans.append([ps,pe])
        return ans
        
# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))