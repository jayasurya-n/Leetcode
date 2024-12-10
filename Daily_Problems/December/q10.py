from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maximumLength(self, s: str) -> int:
        # n = len(s)
        # for l in range(n-1,0,-1):
        #     hash = defaultdict(int)
        #     for start in range(n-l+1):
        #         temp = s[start:start+l]
        #         for k in range(26):
        #             special = "".join([chr(ord('a')+k)]*l)
        #             if(temp==special):
        #                 hash[temp]+=1
        #                 if(hash[temp]>=3):return l
        #                 break
        # return -1
        
        n = len(s)
        curr = s[0]
        ans,cnt = 0,0
        hash = defaultdict(int)
        for ch in s:
            if(curr==ch):cnt+=1
            else:
                ans = max(ans,cnt-2)
                hash["".join([curr]*cnt)]+=1
                if(cnt>1):hash["".join([curr]*(cnt-1))]+=2
                curr = ch
                cnt = 1
        
        ans = max(ans,cnt-2)
        hash["".join([curr]*cnt)]+=1
        if(cnt>1):hash["".join([curr]*(cnt-1))]+=2
        
        for special,val in hash.items():
            if(val>=3):ans = max(ans,len(special))
        return ans if ans!=0 else -1
               
# time complexity: O(n^3),O(n)
# space complexity: O(n^2),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        print(Solution().maximumLength(s))