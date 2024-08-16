from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        size = 100000
        nodes = [sys.maxsize]*(size+1)
        
        q = deque([(start,0)])
        nodes[start] = 0
        
        while q:
            node,steps = q.popleft()
            if(node==end):return steps
            for i in range(len(arr)):
                newNode = (node*arr[i])%size
                if(nodes[newNode]>steps+1):
                    nodes[newNode] = steps+1
                    q.append((newNode,steps+1))
        
        return -1
                

# time complexity: O(n*10**5)
# space complexity: O(n+10**5)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))