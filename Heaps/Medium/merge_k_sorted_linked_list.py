from typing import List,Optional
from collections import deque
import sys, math, heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for ind,node in enumerate(lists):
            if(node):heapq.heappush(pq,(node.val,ind,node))
        
        dummy = ListNode(-1)
        curr = dummy    
        while pq:
            mini,ind,node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            node = node.next
            if(node):heapq.heappush(pq,(node.val,ind,node))
        return dummy.next
            
# time complexity: O(nlogk)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))