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

        def dfs(node,copyNode):
            hash[node] = copyNode
            for v in node.neighbors:
                if(v not in hash):
                    copyV = Node(v.val,None)
                    copyNode.neighbors.append(copyV)
                    dfs(v,copyV)
                else:
                    copyV = hash[v]
                    copyNode.neighbors.append(copyV)
            
        root = Node(node.val,None)  
        hash = dict()
        dfs(node,root)
        return root
                              
# time complexity: O(n+e)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))