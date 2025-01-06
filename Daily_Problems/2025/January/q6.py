from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # ones = [i for i,ch in enumerate(boxes) if ch=='1']
        # j = 0
        # cnt = sum(ones)
        
        # ans = []
        # for i in range(len(boxes)):
        #     if(j<len(ones) and i>ones[j]):
        #         cnt-=2*ones[j]
        #         j+=1
        #     ope = cnt-(len(ones)-j)*i+j*i 
        #     ans.append(ope)
        # return ans
        
        n = len(boxes)
        ans = [0]*n
        
        cnt,ope = 0,0
        for i in range(n):
            ans[i]+=ope
            cnt+=int(boxes[i])
            ope+=cnt
        
        cnt,ope = 0,0
        for i in range(n-1,-1,-1):
            ans[i]+=ope
            cnt+=int(boxes[i])
            ope+=cnt
        return ans

# time complexity: O(n),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))