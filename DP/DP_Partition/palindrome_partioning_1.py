from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def solve(ind,temp):
            if(ind==len(s)):
                ans.append(temp[:])
                return 
            
            for i in range(ind,len(s)):
                sub = s[ind:i+1]
                rsub = s[ind:i+1][::-1]
                if(sub==rsub):
                    temp.append(sub)
                    solve(i+1,temp)
                    temp.pop()
        
        ans = []
        solve(0,[])
        return ans
            
# time complexity: O(n*2^n)
# space complexity: O(n*2^n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))