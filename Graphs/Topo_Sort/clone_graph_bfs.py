from typing import List,Optional
from collections import deque
import sys,math

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']):
        if(node==None):return None
        root = Node(node.val,None)  
        hash = dict([(node,root)])
        q = deque([node])
        
        while q:
            node = q.popleft()
            copyNode = hash[node]
            for v in node.neighbors:
                if(v not in hash):
                    copyV = Node(v.val,[])
                    copyNode.neighbors.append(copyV)
                    hash[v] = copyV
                    q.append(v)
                else:
                    copyV = hash[v]
                    copyNode.neighbors.append(copyV)
        return root                        
# time complexity: O(n+e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))