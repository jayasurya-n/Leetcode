from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1

        ans = 0
        for num in nums:
            if(num==1):
                ans = max(ans,(freq[num] if freq[num]%2==1 else freq[num]-1))
                continue

            cnt = 0
            while freq[num]>1:
                num*=num
                cnt+=2
            ans = max(ans,cnt+(1 if freq[num]>=1 else -1))
        return ans

# time complexity: O(nlog(log(max)))
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))