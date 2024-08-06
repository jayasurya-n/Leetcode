from typing import List,Optional
from collections import deque
import sys
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p==None or q==None):
            return (p==q)
        
        return ((p.val==q.val) and 
        self.isSameTree(p.left,q.left) and 
        self.isSameTree(p.right,q.right))


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = input().strip().split()
        for i in range(len(arr)):
            if(arr[i]!="None"):arr[i]=int(arr[i])
        root = BinaryTree().createBinrayTree(0,None,arr)
        print(Solution().maxPathSum(root))