from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minChanges(self, s: str) -> int:
        # ans,cnt = 0,0
        # curr_ch = s[0]
        
        # for ch in s:
        #     if ch==curr_ch:cnt+=1
        #     else:
        #         if(cnt%2==0):cnt=1
        #         else:
        #             ans+=1
        #             cnt=0
        #     curr_ch = ch
        # return ans
        
        ans = 0
        for i in range(0,len(s),2):
            if(s[i]!=s[i+1]):ans+=1
        return ans
        
# time complexity: O(n),O(n)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))