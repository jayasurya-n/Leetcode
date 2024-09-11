from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head.next==None): return head
        prev = head
        cur = head.next
        while(cur):
            val = math.gcd(prev.val,cur.val)
            node = ListNode(val)
            node.next = cur
            prev.next = node
            prev = cur
            cur = cur.next
        return head 
            
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))