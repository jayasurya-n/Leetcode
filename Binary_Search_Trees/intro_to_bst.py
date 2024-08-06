from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isBSTTraversal(self, arr):
        for i in range(1,len(arr)):
            if(arr[i]<=arr[i-1]):return False
        return True


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))