from typing import List,Optional
from collections import deque
import sys

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):return []
        q = deque()
        q.append(root)
        ans = []

        while(q):
            level = len(q)
            temp = []
            for _ in range(level):
                node = q.popleft()
                temp.append(node.val)
                if(node.left):q.append(node.left)
                if(node.right):q.append(node.right)
            ans.append(temp)
        return ans


# time complexity: O(n)
# space complexity: O(n/2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))