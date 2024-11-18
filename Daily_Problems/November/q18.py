from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0]*n
        if(k==0):return ans
        
        s,e = (1,k) if k>0 else (n+k,n-1)
        sum = 0
        for i in range(s,e+1):sum+=code[i]
        for i in range(n):
            ans[i] = sum
            sum-=code[s%n]
            s+=1
            e+=1
            sum+=code[e%n]
        return ans
        
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))