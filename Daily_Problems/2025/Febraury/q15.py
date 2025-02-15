from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def rec(ind,csum,temp,target,s):
            # if(ind<len(s)):print(temp+[s[ind:]],csum+int(s[ind:]))
            if(ind<len(s) and csum+int(s[ind:])==target):return True
            for i in range(ind,len(s)):
                substring = s[ind:i+1]
                # temp.append(substring)
                csum+=int(substring)
                if(rec(i+1,csum,temp,target,s)):return True
                csum-=int(substring)
                # temp.pop()
            return False
        
        ans = 0
        for num in range(1,n+1):
            if(rec(0,0,[],num,str(num**2))):ans+=num**2
        return ans

# time complexity: O(n*(2**6))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        print(Solution().punishmentNumber(n))