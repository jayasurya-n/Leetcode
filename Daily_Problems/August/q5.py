from typing import List,Optional
from collections import deque
import sys
class Solution:
    def kthDistinct(self, arr: List[str], k: int):
        map = dict()
        for i in range(len(arr)):
            map[arr[i]] = map.get(arr[i],0)+1
        
        for key in map.keys():
            if(map[key]==1):
                k-=1
                if(k==0):return key
        return ""


# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().kthDistinct(arr,k))