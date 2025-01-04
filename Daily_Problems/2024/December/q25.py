from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):return []
        ans = []
        q = deque([root])
        while q:
            maxi = -sys.maxsize
            for _ in range(len(q)):
                node = q.popleft()
                maxi = max(node.val,maxi)
                if(node.left):q.append(node.left)
                if(node.right):q.append(node.right)
            ans.append(maxi)
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))