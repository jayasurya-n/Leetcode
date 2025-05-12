from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # for i in range(len(arr)-2):
        #     if(arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1):return True
        # return False
        
        cnt = 0
        for num in arr:
            if(num%2==1):cnt+=1
            else:cnt=0
            if(cnt==3):return True
        return False

# time complexity: O(n),O(n)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))