from typing import List,Optional
from collections import deque
import sys

class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack1 = []
        self.stack2 = []

        node = root
        while(node):
            self.stack1.append(node)
            node = node.left

        node = root
        while(node):
            self.stack2.append(node)
            node = node.right

    def next(self) -> int:
        node = self.stack1.pop()
        temp = node.right

        while(temp):
            self.stack1.append(temp)
            temp = temp.left
        return node.val

    def before(self) -> int:
        node = self.stack2.pop()
        temp = node.left

        while(temp):
            self.stack2.append(temp)
            temp = temp.right
        return node.val
        

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int):
        obj = BSTIterator(root)
        i = obj.next()
        j = obj.before()

        while(i<j):
            if(i+j==k):return True
            elif(i+j<k):i = obj.next()
            elif(i+j>k):j = obj.before()
        return False


# time complexity: O(n)
# space complexity: O(2h)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))