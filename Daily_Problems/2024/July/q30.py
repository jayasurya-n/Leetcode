from typing import List,Optional
from collections import deque
import sys
class Solution:
    def minimumDeletions(self, s: str):
        a = sum(1 for i in s if i=='a')
        b = 0
        ans = len(s)

        for i in range(len(s)):
            if(s[i]=='a'):a-=1
            ans = min(ans,a+b)
            if(s[i]=='b'):b+=1
        return ans


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))