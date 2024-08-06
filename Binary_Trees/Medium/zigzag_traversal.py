from typing import List,Optional
from collections import deque
import sys
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):return []
        
        ans=[]
        q = deque([root])
        dir = 0
        while(q):
            level = len(q)
            temp = []
            for _ in range(level):
                node = q.popleft()
                temp.append(node.val)
                if(node.left):q.append(node.left)
                if(node.right):q.append(node.right)
            if(dir==1):ans.append(temp[::-1])
            else:ans.append(temp)
            dir^=1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))