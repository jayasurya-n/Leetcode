from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        cnt = 1
        for i in range(1,len(s)):
            if(s[i]!=ans[-1]):cnt=1
            elif(cnt==1 and s[i]==ans[-1]):cnt+=1
            else:continue
            ans+=s[i]
        return ans
            
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))