from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        ans = []
        maxi = items[0][1]
        for i in range(len(items)):
            maxi = max(maxi,items[i][1])
            items[i][1] = maxi
        
        ans = []    
        for q in queries:
            ind = bisect.bisect_right(items,[q,sys.maxsize])-1
            if(ind>=0):ans.append(items[ind][1])
            else:ans.append(0)
        return ans

# time complexity: O(nlogn+qlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))