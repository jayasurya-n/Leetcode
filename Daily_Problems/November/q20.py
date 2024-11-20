from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        f = [0]*3
        for ch in s:f[ord(ch)-ord('a')]+=1
        
        for i in range(3):
            if(f[i]<k):return -1
        
        i,j = 0,0
        w = [0]*3
        ans = 0
        while(j<len(s)):
            w[ord(s[j])-ord('a')]+=1
            while(i<=j and (f[0]-w[0]<k or f[1]-w[1]<k or f[2]-w[2]<k)):
                w[ord(s[i])-ord('a')]-=1
                i+=1
            ans = max(ans,j-i+1)
            j+=1
        return len(s)-ans
                            
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))