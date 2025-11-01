import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: int, head: ListNode) -> ListNode:
        hash = set(nums)
        prev = dummy = ListNode(-1)
        curr = dummy.next = head
        while curr:
            if(curr.val in hash):
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next

# time complexity: O(m)
# space complexity: O(n)
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)