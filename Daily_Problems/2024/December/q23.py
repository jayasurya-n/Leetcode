from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def findMin(arr):
            ans = 0
            original = sorted(arr)
            positions = {val:i for i,val in enumerate(arr)}
            
            for i in range(len(arr)):
                if(original[i]!=arr[i]):
                    ans+=1
                    id = positions[original[i]]
                    positions[arr[i]] = id
                    arr[id],arr[i] = arr[i],arr[id]
            return ans
        
        ans = 0
        q = deque([root])
        while q:
            curr = []
            for _ in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                
                if(node.left):q.append(node.left)
                if(node.right):q.append(node.right)
            ans+=findMin(curr)
        return ans
                
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))