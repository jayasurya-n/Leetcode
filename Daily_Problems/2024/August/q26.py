from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    # def postorder(self, root: 'Node') -> List[int]:
    #     ans = []
    #     def dfs(node):
    #         if(node==None):return
    #         for child in node.children:dfs(child)
    #         ans.append(node.val)
        
    #     dfs(root)
    #     return ans

    def postorder(self, root: 'Node'):
        if(root==None):return []
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if(node.children==None):continue
            for child in node.children:
                stack.append(child)
        return ans[::-1]
            
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))