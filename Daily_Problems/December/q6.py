from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # hash = set()
        # for ele in banned:
        #     if(1<=ele<=n):hash.add(ele)
        
        # sum,cnt = 0,0
        # curr = 1
        # while(sum<maxSum and curr<=n):
        #     if(curr not in hash):
        #         sum+=curr
        #         if(sum<=maxSum):cnt+=1
        #     curr+=1
        # return cnt

        banned.sort()
        sum,cnt = 0,0
        for curr in range(1,n+1):
            ind = bisect.bisect_left(banned,curr)
            if(ind<len(banned) and banned[ind]==curr):continue
            if(sum+curr<=maxSum):
                sum+=curr
                cnt+=1
            else:break
        return cnt

# time complexity: O(m+n),O((m+n)logm)
# space complexity: O(m),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))