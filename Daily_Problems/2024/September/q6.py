from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hash = set(nums)
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head
        while(cur):
            if(cur.val not in hash):
                prev = cur
                cur = cur.next
            else:
                prev.next = cur.next
                cur.next = None
                cur = prev.next
        return dummy.next 
         
# time complexity: O(m+n)
# space complexity: O(m)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))