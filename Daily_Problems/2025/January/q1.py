from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for i in range(len(s)):
            if(s[i]=='1'):ones+=1
        
        ans,zeros = 0,0
        for i in range(len(s)-1):
            if(s[i]=='0'):zeros+=1
            else:ones-=1
            ans = max(ans,zeros+ones)
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))